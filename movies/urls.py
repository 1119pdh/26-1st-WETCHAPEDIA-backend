from django.urls import path

from .views import *


urlpatterns=[
    path("movies/<int:pk>", MovieDetailView.as_view())
]