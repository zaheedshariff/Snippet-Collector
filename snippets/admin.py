from django.contrib import admin
# import your models here
from .models import Snippet, UsageCounter

# Register your models here
admin.site.register(Snippet)
# register the new Feeding Model 
admin.site.register(UsageCounter)