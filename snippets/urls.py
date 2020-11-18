from django.contrib import admin
# Add the include function to the import
from django.urls import path, include

from . import views


urlpatterns = [
  path('', views.home, name='home'),
  path('', views.about, name='about'),
  path('snippets/', views.snippet_index, name='snippets'),
  path('snippets/<int:snippet_id>/', views.snippet_detail, name='detail'),
  path('snippets/create', views.SnippetCreate.as_view(), name='create'),
  path('snippets/<int:pk>/update/', views.SnippetEdit.as_view(), name='snippet_update'),
  path('snippets/<int:pk>/delete/', views.SnippetDelete.as_view(), name='snippet_delete'),
  path('accounts/signup/', views.signup, name='signup'),
  path('snippets/<int:snippet_id>/usage_form/', views.usage_form, name='usage_counter'),
  path('snippets/<int:snippet_id>/assoc_project/<int:uses_id>/', views.assoc_project, name='assoc_project')
]