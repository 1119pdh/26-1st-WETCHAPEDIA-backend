from django.urls import path
<<<<<<< HEAD

from .views import *


urlpatterns=[
    path("/<int:movie_id>", MovieDetailView.as_view())
]
=======
from .views import MovieListView

urlpatterns = [
    path("", MovieListView.as_view()),
]
>>>>>>> main
