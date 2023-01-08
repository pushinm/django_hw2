from django.contrib import admin
from .models import Movie
# Register your models here.

class MovieAdmin(admin.ModelAdmin):
    list_display = ('created_on', 'published_on', 'name', 'rating',)
    list_display_links = ('name',)
    search_fields = ('name', 'rating',)

admin.site.register(Movie, MovieAdmin)