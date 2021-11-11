import json

from django.http       import JsonResponse
from django.views      import View
from django.db.models  import Q, Avg
from json.decoder      import JSONDecodeError

from users.utils       import login_decorater
from .models           import *


class MovieDetailView(View):
    def get(self, request, movie_id):
        try:
            movie   = Movie.objects.get(id=movie_id)
            results = { 
                "movie_basic_info": 
                    {
                        "title"        : movie.title,
                        "release_date" : str(movie.released_at),
                        "genre"        : [genre.name for genre in movie.genres.all()],
                        "country"      : movie.country,
                        "running_time" : movie.running_time_in_minute,
                        "short_comment": movie.description,
                        "poster_url"   : movie.poster_image_url,
                        "grade"        : movie.grade.name,
                        "rate"         : [rate.rate for rate in Rating.objects.filter(movie=movie_id)]
                    }
                    ,    
                "staffs": 
                    [
                        { 
                            "name"             : staff.staff.name, 
                            "position"         : staff.position, 
                            "role"             : staff.role , 
                            "profile_image_url" : staff.staff.profile_image_url
                        }
                        for staff in movie.moviestaff_set.all()
                    ]
                    ,
                "comments": 
                    [
                        {
                            "user_name"  : comment.user.name,
                            "comment"    : comment.description,
                            "like_number": LikeComment.objects.filter(comment = comment).count()
                        } 
                        for comment in Comment.objects.filter(movie=movie_id)
                    ]
            }
            return JsonResponse({"movie" : results}, status=200)

        except KeyError:
            return JsonResponse({"message" : "KEY_ERROR"}, status=400)

        except Movie.DoesNotExist:
            return JsonResponse({"message" : "영화 정보가 없습니다."}, status=404)

class MovieListView(View):
    def get(self, request):
        source  = request.GET.get("source")
        rating  = request.GET.get("rating")
        keyword = request.GET.get("keyword")
        OFFSET  = int(request.GET.get("offset", 0))
        LIMIT   = int(request.GET.get("display", 15))

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
    
class CommentView(View):
    @login_decorater
    def post(self, request, movie_id):
        
        try:
            data = json.loads(request.body)

            Comment.objects.create(
                user_id     = request.user.id,
                movie_id    = movie_id,
                description = data['description']
            )
            
            return JsonResponse({'message' : 'SUCCESS'}, status = 201)
        
        except JSONDecodeError:
            return JsonResponse({"message" : "JSON_DECODE_ERROR"}, status=400)
        except KeyError:
            return JsonResponse({'message' : 'KEY_ERROR'}, status = 400)

    @login_decorater
    def put(self, request, movie_id):
        
        try:
            data         = json.loads(request.body)
            user_id      = request.user.id
            comment_info = Comment.objects.get(user_id = user_id, movie_id = movie_id)
            
            comment_info.description = data['description']
            comment_info.save()
            
            return JsonResponse({'message' : 'SUCCESS'}, status = 200)
        
        except JSONDecodeError:
            return JsonResponse({"message" : "JSON_DECODE_ERROR"}, status=400)
        except KeyError:
            return JsonResponse({'message' : 'KEY_ERROR'}, status = 400)
        
    @login_decorater
    def delete(self, request, movie_id):
        
        try:
            user_id      = request.user.id
            comment_info = Comment.objects.get(user_id = user_id, movie_id = movie_id)
            
            comment_info.delete()
        
            return JsonResponse({'message' : 'SUCCESS'}, status = 204)
        
        except Comment.DoesNotExist:
            return JsonResponse({'message' : 'INVALID_COMMENT'}, status = 404)
        
    @login_decorater
    def get(self, request, movie_id):
        
        try:
            user_id      = request.user.id
            comment_info = Comment.objects.get(user_id = user_id, movie_id = movie_id)
            result       = comment_info.description
        
            return JsonResponse({'description' : result}, status = 200)
        
        except Comment.DoesNotExist:
            return JsonResponse({'message' : 'INVALID_COMMENT'}, status = 404)