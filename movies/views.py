from django.shortcuts import redirect
from django.views.generic import ListView, DetailView
from django.views.generic.base import View

from movies.models import Movie
from .forms import ReviewForm


# GenreYear
# MoviesView
# MovieDetailView
# AddReview
# ActorView
# FilterMoviesView
# JsonFilterMoviesView
# AddStarRating
# Search


class MoviesView(ListView):
    """ Список фильмов """
    model = Movie
    queryset = Movie.objects.filter(draft=False)
    # context_object_name = 'movies'


class MovieDetailView(DetailView):
    """ Полное описание фильма"""
    model = Movie
    slug_field = 'url'


class AddReview(View):
    """Отзывы"""

    def post(self, request, pk):
        form = ReviewForm(request.POST)
        movie = Movie.objects.get(id=pk)
        if form.is_valid():
            form = form.save(commit=False)
            form.movie = movie
            form.save()
        return redirect(movie.get_absolute_url())
