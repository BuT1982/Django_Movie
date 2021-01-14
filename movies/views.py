
from django.views.generic import ListView, DetailView
from movies.models import Movie


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
