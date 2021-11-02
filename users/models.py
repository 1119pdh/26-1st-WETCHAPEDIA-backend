from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=50)
    password = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    profile_image_url = models.URLField(max_length=2000, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "users"
