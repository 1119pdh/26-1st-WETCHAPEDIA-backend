import json, bcrypt, jwt

from django.http    import JsonResponse
from django.views   import View

from users.models   import User
from users.utils    import validate_email, validate_password
from django.conf    import settings

class SignUpView(View):
    def post(self, request):

        try:
            data     = json.loads(request.body)
            name     = data['name']
            password = data['password']
            email    = data['email']

            if not validate_email(email):
                return JsonResponse({'message':'EMAIL_NOT_VALID'}, status = 400)

            if not validate_password(password):
                return JsonResponse({'message':'PASSWORD_NOT_VALID'}, status = 400)

            if User.objects.filter(email=email).exists():
                return JsonResponse({'message' : 'SAME_VALUE_ERROR'}, status = 400)

            hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

            User.objects.create(
                name     = name,
                password = hashed_password,
                email    = email
            )

            return JsonResponse({'message' : 'SUCCESS'}, status = 201)

        except KeyError:
            return JsonResponse({'message' : 'KEY_ERROR'}, status = 400)

class SignInView(View):
    def post(self, request):

        try:
            data         = json.loads(request.body)
            password     = data['password']
            email        = data['email']
            user         = User.objects.get(email=email)
            access_token = jwt.encode({'user_id' : user.id}, settings.SECRET_KEY, settings.ALGORITHM)

            if not bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8')):
                return JsonResponse({'message' : 'INVALID_USER'}, status = 401)

            return JsonResponse({'message' : 'SUCCESS', 'ACCESS_TOKEN' : access_token}, status = 200)

        except KeyError:
            return JsonResponse({'message': 'KEY_ERROR'}, status = 400)
        except User.DoesNotExist :
            return JsonResponse({"message" : "Unauthorized"}, status = 401) 