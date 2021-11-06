from django.http import JsonResponse
from django.views import View
from django.db.models import Q, Avg
from .models import *


class MovieListView(View):
    def get(self, request):
        LIMIT = 15
        OFFSET = 0
        source = request.GET.get("source")
        staff = request.GET.get("staff")
        title = request.GET.get("title")
        rating = request.GET.get("rating")

        q = Q()
        if source:
            q.add(Q(sources__name=source), q.AND)

        if staff:
            q.add(Q(staffs__name=staff), q.AND)

        if title:
            q.add(Q(title__icontains=title), q.AND)

        if rating:
            q = Q()

        movies = (
            Movie.objects.filter(q)
            .annotate(average_point=Avg("rating__rate"))
            .order_by("-average_point")[OFFSET:LIMIT]
        )

        result = {
            "movies": [
                {
                    "id": movie.id,
                    "title": movie.title,
                    "poster_image_url": movie.poster_image_url,
                    "released_at": movie.released_at,
                    "country": movie.country,
                    "ratings": movie.average_point,
                    "sources": [source.name for source in movie.sources.all()],
                }
                for movie in movies
            ]
        }

        return JsonResponse({"message": result}, status=200)
