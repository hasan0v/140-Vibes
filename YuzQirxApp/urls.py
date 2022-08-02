from re import template
from django.urls import path
from . import views
from .views import Home, Tracks, TrackDetail 

urlpatterns=[
    path(r'', Home.as_view(), name='home'),
    path(r'tracks', Tracks.as_view(), name='tracks'),
    path(r'track/<int:pk>', TrackDetail.as_view(), name='track'),
    # path(r'c', Home(), name='team'),
    # path(r'd', Home(), name='home'),
    # path(r'f', Home(), name='about'),
]