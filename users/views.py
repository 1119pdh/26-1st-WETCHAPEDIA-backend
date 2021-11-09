import json, bcrypt, jwt

from django.http import JsonResponse
from django.views import View

from users.models import User
from movies.models import Movie, WishList
from users.utils import validate_email, validate_password, login_decorater
from django.conf import settings


class SignUpView(View):
    def post(self, request):

        try:
            data = json.loads(request.body)
            name = data["name"]
            password = data["password"]
            email = data["email"]

            if not validate_email(email):
                return JsonResponse({"message": "EMAIL_NOT_VALID"}, status=400)

            if not validate_password(password):
                return JsonResponse({"message": "PASSWORD_NOT_VALID"}, status=400)

            if User.objects.filter(email=email).exists():
                return JsonResponse({"message": "DUPLICATE_EMAIL_ERROR"}, status=400)

            hashed_password = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")

            User.objects.create(name=name, password=hashed_password, email=email)

            return JsonResponse({"message": "SUCCESS"}, status=201)

        except KeyError:
            return JsonResponse({"message": "KEY_ERROR"}, status=400)


class SignInView(View):
    def post(self, request):

        try:
            data = json.loads(request.body)
            password = data["password"]
            email = data["email"]
            user = User.objects.get(email=email)
            access_token = jwt.encode({"user_id": user.id}, settings.SECRET_KEY, settings.ALGORITHM)

            if user.deleted_at != None:
                return JsonResponse({"message": "UNACTIVATED_USER"}, status=403)

            if not bcrypt.checkpw(password.encode("utf-8"), user.password.encode("utf-8")):
                return JsonResponse({"message": "INVALID_USER"}, status=401)

            return JsonResponse({"message": "SUCCESS", "access_token": access_token}, status=200)

        except KeyError:
            return JsonResponse({"message": "KEY_ERROR"}, status=400)
        except User.DoesNotExist:
            return JsonResponse({"message": "Unauthorized"}, status=401)


class WishListView(View):
    @login_decorater
    def post(self, request):
        data = json.loads(request.body)
        movie_id = data["movie_id"]
        if not WishList.objects.filter(movie_id=movie_id, user_id=request.user.id).exists():
            WishList.objects.create(user=request.user, movie=Movie.objects.get(id=movie_id))
            return JsonResponse({"message": "WISHLIST_CREATE_SUCCESS"}, status=201)

        wishlist_data = WishList.objects.get(movie_id=movie_id, user_id=request.user.id)
        wishlist_data.delete()

        return JsonResponse({"message": "WISHLIST_DELETE_SUCCESS"}, status=200)

    @login_decorater
    def get(self, request):
        wishlists = WishList.objects.filter(user_id=request.user.id)
        result = [
            {
                "id": wishlist.movie.id,
                "title": wishlist.movie.title,
                "poster_url": wishlist.movie.poster_image_url,
            }
            for wishlist in wishlists
        ]
        return JsonResponse({"MESSAGE": result}, status=200)
