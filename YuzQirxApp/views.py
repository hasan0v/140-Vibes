from django.shortcuts import render
from django.views.generic import ListView, DetailView
# from django.urls import reverse
# from django.http import HttpResponseRedirect
from .models import Track, Album, Profile, Product, ProductImage
from .tools import get_video_stats, standardizer
# from django.views.decorators.csrf import csrf_exempt


class Home(ListView):
    model=Profile
    template_name='home.html'
    def get_context_data(self,*args, **kwargs):
        artists = Profile.objects.all()
        artists_ids = Profile.objects.values_list('id', flat=True)
        ids = []
        for i in artists_ids:
            ids.append(i)
        print(ids)
        context = super(Home, self).get_context_data(*args, **kwargs)
        context["artists"] = artists
        context["ids"] = ids
        return context
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
            try:
                videos.append(track.youtube_link.replace('https://www.youtube.com/watch?v=',''))
            except:
                pass
        views, likes = get_video_stats(videos)
        views = standardizer(views)
        likes = standardizer(likes)
        context["tracks"] = tracks
        context["views"] = views
        context["likes"] = likes
        return context

class Store(ListView):
    model=Product
    template_name='store.html'
    def get_context_data(self,*args, **kwargs):
        products = Product.objects.all().order_by('-price')
        # image_product = {}
        for p in products:
            images = ProductImage.objects.filter(product=p).first()
            p.image = images.image.url
            print("proo", p.image)


        context = super(Store, self).get_context_data(*args, **kwargs)
        context["products"] = products
        return context
class ProductDetail(DetailView):
    model=Product
    template_name='product.html'
    
    def get_context_data(self,*args, **kwargs):
        product =  Product.objects.get(id=self.kwargs['pk'])
        imagefirst = ProductImage.objects.filter(product=product).first()
        images = ProductImage.objects.filter(product=product)[1:]
        context = super(ProductDetail, self).get_context_data(*args, **kwargs)
        context["product"] = product
        context["imagefirst"] = imagefirst
        context["images"] = images
        return context
def ProfileDetail(request, name):
    profile =  Profile.objects.filter(name=name).first()
    tracks =  Track.objects.filter(author=name)
    track_list = tracks.all()
    videos = []
    for track in track_list:
        try:
            videos.append(track.youtube_link.replace('https://www.youtube.com/watch?v=',''))
        except:
            pass
    views, likes = get_video_stats(videos)
    views = standardizer(views)
    likes = standardizer(likes)
    return render(request, 'profile.html', {'profile':profile, 'likes':likes, 'views':views, 'tracks':track_list})

# def AddCart(request, id):
#     product = Product.objects.get(id=id)
#     if request.user.is_authenticated:
#         profile = Profile.objects.get(user=request.user)
#         profile.cart.add(product)
#         profile.save()
#     cart = []
#     return HttpResponseRedirect(reverse('store', {'cart':cart}))

def About(request):
    return render(request, 'about.html')
    