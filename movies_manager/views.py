from django.shortcuts import render
# from django.http import (HttpResponse,)
# from django.template import loader
# Create your views here.
from .models import Movie

'''def index(request) -> HttpResponse:
    response_ = 'Список фильмов с рейтингом в фильмотеке \r\n\r\n'
    for item_movie in Movie.objects._order_by('-pk'):
        response_ += item_movie.name + '\r\n' + str(item_movie.rating) + '%\r\n'
    return HttpResponse(response_, content_type='text/plain;charset=utf8')'''

'''def index(request) -> HttpResponse:
    template_ = loader.get_template('index.html')
    movies = Movie.objects.order_by('-pk')
    context = {'movies':movies}

    return HttpResponse(template_.render(context, request))'''

def by_director(request, director_pk) -> render:
    template_ = 'by_director.html'
    movies = Movie.objects.filter(director=director_pk)

    context = {
        'movies': movies,
    }

    return render(request, template_, context=context)

def index(request) -> render:

    template_ = 'index.html'
    movies = Movie.objects.order_by('-pk')
    context = {
        'movies': movies
               }

    return render(request, template_, context=context)


