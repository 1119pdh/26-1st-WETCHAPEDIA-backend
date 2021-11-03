from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=50)
    poster_image_url = models.URLField(max_length=2000)
    country = models.CharField(max_length=50)
    description = models.TextField()
    running_time_in_minute = models.IntegerField()
    released_at = models.DateField()
    grade = models.ForeignKey("Grade", on_delete=models.CASCADE)
    sources = models.ManyToManyField("Source", through="MovieSource", related_name="sources")
    genres = models.ManyToManyField("Genre", through="MovieGenre", related_name="genres")
    staffs = models.ManyToManyField("Staff", through="MovieStaff", related_name="staffs")
    ratings = models.ManyToManyField("users.User", through="Rating", related_name="ratings")
    wishlists = models.ManyToManyField("users.User", through="WishList", related_name="wishlists")
    comments = models.ManyToManyField("users.User", through="Comment", related_name="comments")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "movies"


class Grade(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        db_table = "grades"


class Source(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        db_table = "sources"


class MovieSource(models.Model):
    movie = models.ForeignKey("Movie", on_delete=models.CASCADE)
    source = models.ForeignKey("Source", on_delete=models.CASCADE)

    class Meta:
        db_table = "movie_sources"


class Staff(models.Model):
    name = models.CharField(max_length=50)
    profile_image_url = models.URLField(max_length=2000)

    class Meta:
        db_table = "staffs"


class MovieStaff(models.Model):
    staff = models.ForeignKey("Staff", on_delete=models.CASCADE)
    movie = models.ForeignKey("Movie", on_delete=models.CASCADE)
    role = models.CharField(max_length=50)
    position = models.CharField(max_length=50)

    class Meta:
        db_table = "movie_staffs"


class Rating(models.Model):
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    movie = models.ForeignKey("Movie", on_delete=models.CASCADE)
    rate = models.DecimalField(max_digits=2, decimal_places=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "ratings"


class WishList(models.Model):
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    movie = models.ForeignKey("Movie", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "whislists"


class Genre(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        db_table = "genres"


class MovieGenre(models.Model):
    movie = models.ForeignKey("Movie", on_delete=models.CASCADE)
    genre = models.ForeignKey("Genre", on_delete=models.CASCADE)

    class Meta:
        db_table = "movie_genres"


class Comment(models.Model):
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    movie = models.ForeignKey("Movie", on_delete=models.CASCADE)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "comments"


class LikeComment(models.Model):
    comment = models.ForeignKey("Comment", on_delete=models.CASCADE)
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)

    class Meta:
        db_table = "like_comments"
