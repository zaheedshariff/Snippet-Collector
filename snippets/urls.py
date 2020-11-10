from django.contrib import admin
# Add the include function to the import
from django.urls import path, include

from . import views


urlpatterns = [
  path('', views.home, name='home'),
  path('snippets/', views.snippet_index, name='snippets'),
  path('login/', views.login, name='login'),
  path('snippets/<int:snippet_id>/', views.snippet_detail, name='detail')
]