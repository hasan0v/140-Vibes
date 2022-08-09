from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from .models import Track, Album, Profile
from django.db import connection
from .tools import dictfetchall, get_video_stats, standardizer
from django.views.decorators.csrf import csrf_exempt
import requests
from bs4 import BeautifulSoup
# Create your views here.
# class HomeView(ListView):
    # model=Track
    # template_name='home.html'
    # ordering=['-created_at']
    # def get_context_data(self,*args, **kwargs):
    #     cat_menu = Categorie.objects.all()
    #     context = super(HomeView, self).get_context_data(*args, **kwargs)
    #     context["cat_menu"] = cat_menu
    #     return context
    # ""

# @csrf_exempt


class Home(ListView):
    model=Album
    template_name='home.html'

class Tracks(ListView):
    model=Track
    template_name='tracks.html'
    def get_context_data(self,*args, **kwargs):
        tracks = Track.objects.all().order_by('-created_at')
        context = super(Tracks, self).get_context_data(*args, **kwargs)
        context["tracks"] = tracks
        return context
class Albums(ListView):
    model=Album
    template_name='albums.html'
    def get_context_data(self,*args, **kwargs):
        albums = Album.objects.all().order_by('-created_at')
        context = super(Albums, self).get_context_data(*args, **kwargs)
        context["albums"] = albums
        return context


class TrackDetail(DetailView):
    model=Track
    template_name='track.html'
    
    def get_context_data(self,*args, **kwargs):
        track =  Track.objects.get(id=self.kwargs['pk'])
        context = super(TrackDetail, self).get_context_data(*args, **kwargs)
        video = []
        video.append(track.youtube_link.replace('https://www.youtube.com/watch?v=',''))
        views, likes = get_video_stats(video)
        views = standardizer(views)
        likes = standardizer(likes)
        context["track"] = track
        context["views"] = views
        context["likes"] = likes
        return context
class AlbumDetail(DetailView):
    model=Album
    template_name='album.html'
    
    def get_context_data(self,*args, **kwargs):
        album =  Album.objects.get(id=self.kwargs['pk'])
        tracks =  Track.objects.filter(album=album)
        track_list = tracks.all()
        context = super(AlbumDetail, self).get_context_data(*args, **kwargs)
        videos = []
        for track in track_list:
            videos.append(track.youtube_link.replace('https://www.youtube.com/watch?v=',''))
        views, likes = get_video_stats(videos)
        views = standardizer(views)
        likes = standardizer(likes)
        print("loho", views, likes)
        context["tracks"] = tracks
        context["views"] = views
        context["likes"] = likes
        return context

def ProfileDetail(request, name):
    profile =  Profile.objects.filter(name=name)
    tracks =  Track.objects.filter(author=name)
    track_list = tracks.all()
    videos = []
    for track in track_list:
        videos.append(track.youtube_link.replace('https://www.youtube.com/watch?v=',''))
    views, likes = get_video_stats(videos)
    views = standardizer(views)
    likes = standardizer(likes)
    return render(request, 'profile.html', {'profile':profile, 'likes':likes, 'views':views, 'tracks':track_list})

    