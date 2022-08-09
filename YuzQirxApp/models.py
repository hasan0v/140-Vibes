from email.mime import image
from gettext import install
import re
from unicodedata import name
from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from datetime import date, datetime
# Create your models here.
class Track(models.Model):
    name=models.CharField(max_length=255, null=False, blank=False)
    beat=models.CharField(max_length=255, null=True, blank=True)
    author=models.CharField(max_length=255, null=False, blank=False)
    feat=models.CharField(max_length=255, null=True, blank=True)
    music_producer=models.CharField(max_length=255, null=True, blank=True)
    executive_producer=models.CharField(max_length=255, null=True, blank=True)
    cover_designer=models.CharField(max_length=255, null=True, blank=True)
    cover=models.ImageField(null=True, blank=True, upload_to="music/covers")
    spotify_link=models.CharField(max_length=255, null=True, blank=True)
    apple_music_link=models.CharField(max_length=255, null=True, blank=True)
    youtube_link=models.CharField(max_length=255, null=True, blank=True)
    tidal_link=models.CharField(max_length=255, null=True, blank=True)
    amazon_link=models.CharField(max_length=255, null=True, blank=True)
    soundcloud_link=models.CharField(max_length=255, null=True, blank=True)
    youtube_music_link=models.CharField(max_length=255, null=True, blank=True)
    deezer_link=models.CharField(max_length=255, null=True, blank=True)
    qobuz_link=models.CharField(max_length=255, null=True, blank=True)
    napster_link=models.CharField(max_length=255, null=True, blank=True)
    yandex_music_link=models.CharField(max_length=255, null=True, blank=True)
    itunes_buy_link=models.CharField(max_length=255, null=True, blank=True)
    amazon_buy_link=models.CharField(max_length=255, null=True, blank=True)
    created_at=models.DateField()
    lyrics=RichTextField(blank=True, null=True, max_length=10000)
    demo=models.FileField(null=False, blank=False, upload_to='demolar/')
    album=models.CharField(max_length=255, null=True, blank=True)
    def __str__(self):
        return self.name

class Profile(models.Model):
    user=models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name=models.CharField(max_length=255, null=False, blank=False)
    profile_pic=models.ImageField(null=True, blank=True, upload_to="images/prof_pics")
    spotify_profile=models.CharField(max_length=255, null=True, blank=True)
    apple_music_profile=models.CharField(max_length=255, null=True, blank=True)
    deezer_profile=models.CharField(max_length=255, null=True, blank=True)
    yandex_music_profile=models.CharField(max_length=255, null=True, blank=True)
    youtube_profile=models.CharField(max_length=255, null=True, blank=True)
    tidal_profile=models.CharField(max_length=255, null=True, blank=True)
    soundcloud_profile=models.CharField(max_length=255, null=True, blank=True)
    instagram_profile=models.CharField(max_length=255, null=True, blank=True)
    twitter_profile=models.CharField(max_length=255, null=True, blank=True)
    facebook_profile=models.CharField(max_length=255, null=True, blank=True)
    def __str__(self):
        return self.name

class Album(models.Model):
    name=models.CharField(max_length=255, null=True, blank=True)
    author=models.CharField(max_length=255, null=True, blank=True)
    created_at=models.DateField()
    executive_producer=models.CharField(max_length=255, null=True, blank=True)
    cover_designer=models.CharField(max_length=255, null=True, blank=True)
    cover=models.ImageField(null=True, blank=True, upload_to="music/covers")
    spotify_link=models.CharField(max_length=255, null=True, blank=True)
    youtube_link=models.CharField(max_length=255, null=True, blank=True)
    soundcloud_link=models.CharField(max_length=255, null=True, blank=True)
    deezer_link=models.CharField(max_length=255, null=True, blank=True)
    apple_music_link=models.CharField(max_length=255, null=True, blank=True)
    yandex_music_link=models.CharField(max_length=255, null=True, blank=True)
    def __str__(self):
        return self.name