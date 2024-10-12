from django.db import models
from django.contrib.auth.models import User

class UserLogin(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100) 

    def __str__(self):
        return self.username

class Movie(models.Model):
    title = models.CharField(max_length=100)
    poster = models.ImageField(upload_to='images/POSTER/')
    # อื่นๆ เช่น รายละเอียดหนัง, ปี, ประเภท เป็นต้น
    poster = models.ImageField(upload_to='posters/')
    def __str__(self):
        return self.title

class FavoriteMovie(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'movie')

    def __str__(self):
        return f"{self.user.username}'s favorite: {self.movie.title}"
