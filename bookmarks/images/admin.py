from django.contrib import admin
from .models import Image

@admin.register(Image)
class ImagesAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'image', 'created']
    list_filter = ['created']
