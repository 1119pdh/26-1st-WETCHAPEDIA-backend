from django.urls import path

from .views import *


urlpatterns=[
    path("movies/<int:movie_id>", MovieDetailView.as_view())
]