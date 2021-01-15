from django.urls import path

from . import views
from .views import MoviesView, MovieDetailView

urlpatterns = [
    path('', MoviesView.as_view()),
    path('<slug:slug>/', MovieDetailView.as_view(), name='movie_detail'),
    path("review/<int:pk>/", views.AddReview.as_view(), name="add_review"),
]
