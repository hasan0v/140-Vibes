from re import template
from django.urls import path
from . import views
from .views import Home, Tracks, Albums, TrackDetail, AlbumDetail, ProfileDetail

urlpatterns=[
    path(r'', Home.as_view(), name='home'),
    path(r'tracks', Tracks.as_view(), name='tracks'),
    path(r'albums', Albums.as_view(), name='albums'),
    path(r'track/<int:pk>', TrackDetail.as_view(), name='track'),
    path(r'album/<int:pk>', AlbumDetail.as_view(), name='album'),
    path(r'profile/<str:name>', ProfileDetail, name='profile'),
]