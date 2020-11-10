from django.db import models

# Create your models here.
class Snippet(models.Model):
    lanaguage = models.CharField(max_length=50)
    category = models.CharField(max_length=200)
    description = models.TextField()
    year_discovered = models.IntegerField()