from django.db import models
from musician.models import Musician

class Album(models.Model):
    album_name = models.CharField(max_length=50)
    musician = models.ForeignKey(
        Musician,
        on_delete=models.CASCADE,
        related_name="albums"
    )
    album_release_date = models.DateField()
    RATING_CHOICES = [
        (1, '★☆☆☆☆'),
        (2, '★★☆☆☆'),
        (3, '★★★☆☆'),
        (4, '★★★★☆'),
        (5, '★★★★★')
    ]
    rating = models.IntegerField(choices=RATING_CHOICES)

    def __str__(self):
        return self.album_name
