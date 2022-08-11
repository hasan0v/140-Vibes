from django.contrib import admin
from .models import Product, Track, Album, Profile, Size, Color, Product, ProductImage
# Register your models here.

admin.site.register(Track)
admin.site.register(Album)
admin.site.register(Profile)
admin.site.register(Product)
admin.site.register(ProductImage)
admin.site.register(Size)
admin.site.register(Color)