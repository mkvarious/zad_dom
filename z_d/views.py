from django.shortcuts import render
from django.views import View
from .models import Movie
from django.template import RequestContext
from .models import Person
from .models import Genre
from django.http import HttpResponse


class MoviesView(View):
    def get(self, request):
        movies = Movie.objects.order_by("year")
        return render(request, "movies.html", context={"movie": movies})

    def post(rself, request):
        title = request.POST.get("movie title")
        director = request.POST.get("director")
        screenplay = request.POST.get("screenplay")
        starring = request.POST.get("starring")
        year = request.POST.get("year")
        rating = request.POST.get("rating")
        genre = request.POST.get("genre")
        Movie.objects.create(title=title, director=director, screenplay=screenplay, starring=starring, year=year, rating=rating, genre=genre)
        return render(request, "movies.html")

class SortDescendingView(View):
    def get(self, request):
        movies = Movie.objects.order_by("year")
        return render(request, "movies.html", context={"movie": movies})

    def post(self, request):
        type = request.POST.get("sortType")
        if type == "malejąco":
            desc = Movie.objects.order_by("rating")
            return HttpResponse(request, "movies.html", context={"desc": desc})

class SearchMoviesView(View):
    def get(rself, request):
        title = request.GET.get("title")
        #first_name = request.GET.get("first_name")
        #second_name = request.GET.get("second_name")
        #year = request.GET.get("year")
        #rating = request.GET.get("rating")
        #genre = request.GET.get("genre")

        movies = Movie.objects.all()
        if title:
            movies.filter(title__contains=title)
        return render(request, "search_movie.html", context = {"movies": movies})

