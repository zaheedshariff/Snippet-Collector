from django.db import models
from django.urls import reverse
from datetime import date

from django.contrib.auth.models import User

PROJECTS = (
    ('W', 'Workshopping'),
    ('G', 'Game'),
    ('P', 'Productivity'),
)

# can be used on different projects
class Use(models.Model):
    link = models.CharField(max_length=200)

# Create your models here.
class Snippet(models.Model):
    language = models.CharField(max_length=50)
    type = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    description = models.TextField()
    year_discovered = models.IntegerField() 
    Uses = models.ManyToManyField(Use)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def get_absolute_url(self):
        return reverse('detail', kwargs={'snippet_id': self.id})
    def __str__(self):
        return self.language
    def last_used(self):    
        return self.usagecounter_set.filter(date=date.today()).count() >= len(PROJECTS)


class UsageCounter(models.Model):
    date = models.DateField('Usage Date')
    type = models.CharField(
    max_length=1,
    # add the 'choices' field option
    choices=PROJECTS,
    # set the default value for meal to be 'B'
    default=PROJECTS[0][0]
  )
    snippet = models.ForeignKey(Snippet, on_delete=models.CASCADE)

    def __str__(self):
    # Nice method for obtaining the friendly value of a Field.choice
        return f"{self.get_type_display()} on {self.date}"
      # change the default sort
    class Meta:
        ordering = ['-date']

