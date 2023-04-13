
from django.db import models
from movies.models import Movie
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator


User  = get_user_model()


class Like(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='likes')
    is_like = models.BooleanField(default=False)
    def __str__(self):
        return f'{self.owner} liked - {self.movie.title}'

class Rating(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE,related_name='ratings')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='ratings')
    rating = models.SmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], blank=True, null=True)

    def __str__(self):
        return f'{self.owner} --> {self.movie.title}'
    
class Favorite(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='favorites')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favorites')

    def __str__(self):
        return f'{self.owner} --> {self.movie.title}'
    
