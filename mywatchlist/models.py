from platform import release
from django.db import models

# Create your models here.
class MyWatchList(models.Model):
    watched = models.TextField()
    title = models.TextField()
    rating = models.IntegerField()
    release_date = models.DateField()
    review = models.TextField()