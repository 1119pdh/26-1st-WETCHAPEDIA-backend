from django.urls import path, include

urlpatterns = [
    path("", include("movies.urls")),
    path("users", include("users.urls")),
]
