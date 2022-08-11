from django.urls import path
from .views import Home, Tracks, Albums, TrackDetail, AlbumDetail, ProfileDetail, Store, ProductDetail, About #, AddCart

urlpatterns=[
    path(r'', Home.as_view(), name='home'),
    path(r'tracks', Tracks.as_view(), name='tracks'),
    path(r'about', About, name='about'),
    path(r'albums', Albums.as_view(), name='albums'),
    path(r'store', Store.as_view(), name='store'),
    path(r'track/<int:pk>', TrackDetail.as_view(), name='track'),
    path(r'album/<int:pk>', AlbumDetail.as_view(), name='album'),
    path(r'product/<int:pk>', ProductDetail.as_view(), name='product'),
    path(r'profile/<str:name>', ProfileDetail, name='profile'),
    # path(r'cart/<int:pk>', AddCart, name='cart'),
]