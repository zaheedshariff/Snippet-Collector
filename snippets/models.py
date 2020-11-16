from django.db import models
from django.urls import reverse
from datetime import date

from django.contrib.auth.models import User

PROJECTS = (
    ('W', 'Workshopping'),
    ('G', 'Game'),
    ('P', 'Productivity'),
)

# Create your models here.
class Snippet(models.Model):
    language = models.CharField(max_length=50)
    type = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    description = models.TextField()
    year_discovered = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # Method added to class
    def get_absolute_url(self):
        return reverse('detail', kwargs={'snippet_id': self.id})
    def __str__(self):
        return self.language

class UsageCounter(models.Model):
    date = models.DateField('Usage Date')
    type = models.CharField(max_length=10)
    snippet = models.ForeignKey(Snippet, on_delete=models.CASCADE)

    def __str__(self):
    # Nice method for obtaining the friendly value of a Field.choice
        return f"{self.get_type_display()} on {self.date}"





# class Project(models.Model):
#     name = models.CharField(max_length=100)
#     date_used = models.IntegerField()
#     project_description = models.TextField()
#     link = models.CharField(max_length=300)
#     Project = models.ForeignKey(Snippet,on_delete=models.CASCADE)


