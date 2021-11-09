from django.urls import path

from .views import *


urlpatterns=[
    path("", MovieListView.as_view()),
    path("/<int:movie_id>", MovieDetailView.as_view()),
    path("/rate/<int:movie_id>", RateListView.as_view())
]