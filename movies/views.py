from django.http import JsonResponse
from django.views import View
from django.db.models import Q, Avg
from .models import *


class MovieListView(View):
    def get(self, request):
        source = request.GET.get("source")
        rating = request.GET.get("rating")
        keyword = request.GET.get("keyword")
        OFFSET = int(request.GET.get("offset", 0))
        LIMIT = int(request.GET.get("display", 15))

        category = {
            "박스오피스": "박스오피스 영화 순위",
            "왓챠": "왓챠 영화 순위",
            "넷플릭스": "넷플릭스 영화 순위",
            "평균별점": "평균별점이 높은 작품",
        }

        result = {}

        q = Q()

        if source:
            q.add(Q(sources__name=source), q.AND)
            result["category"] = category[source]

        if keyword:
            q.add(Q(staffs__name__icontains=keyword) | Q(title__icontains=keyword), q.AND)

        if rating:
            q = Q()
            result["category"] = category[rating]

        movies = (
            Movie.objects.filter(q)
            .annotate(average_point=Avg("rating__rate"))
            .order_by("-average_point")[OFFSET : OFFSET + LIMIT]
        )

        result["movies"] = [
            {
                "id": movie.id,
                "title": movie.title,
                "poster_image_url": movie.poster_image_url,
                "released_at": movie.released_at,
                "country": movie.country,
                "ratings": round(movie.average_point, 1) if movie.average_point != None else 0,
                "sources": [source.name for source in movie.sources.all()],
            }
            for movie in movies
        ]

        return JsonResponse({"message": result}, status=200)
