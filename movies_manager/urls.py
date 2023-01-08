from django.urls import path
from .views import index, by_director

urlpatterns = [
    path('', index, name='index'),
    path('director/<int:director_pk>', by_director, name='by_director'),
]
