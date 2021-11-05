import json, re

from django.conf  import settings
from django.http  import JsonResponse, request
from django.views import View

from .models      import Comment, LikeComment, Movie, Rating


class MovieDetailView(View):
    def get(self, request, pk):
        try:
            results = []
            movie   = Movie.objects.get(id=pk)
            results.append(
                {
                "movieBasicInfo": 
                    {
                    "title"       : movie.title,
                    "release_date": str(movie.released_at),
                    "genre"       : [genre.name for genre in movie.genres.all()],
                    "country"     : movie.country,
                    "runningTime" : movie.running_time_in_minute,
                    "shortcomment": movie.description,
                    "poster_url"  : movie.poster_image_url,
                    "grade"       : movie.grade.name,
                    "rate"        : [rate.rate for rate in Rating.objects.filter(movie=pk)]
                    ,
                    "staffs": 
                        [
                            { 
                            "name"              : staff.staff.name, 
                            "position"          : staff.position, 
                            "role"              : staff.role , 
                            "profile_image_url" : staff.staff.profile_image_url
                            }
                        for staff in movie.moviestaff_set.all()
                        ]
                    },
                "comments": 
                    [
                        {
                            "userName"  : comment.user.name,
                            "comment"   : comment.description,
                            "likeNumber": LikeComment.objects.filter(comment = comment).count()
                        } 
                        for comment in Comment.objects.filter(movie=pk)
                    ]
                }
            )   
            return JsonResponse({"movie" : results}, status= 200)

        except KeyError:
            return JsonResponse({"message" : "KEY_ERROR"}, status=400)

        except Movie.DoesNotExist:
            return JsonResponse({"message" : "영화 정보가 없습니다."}, status=401)