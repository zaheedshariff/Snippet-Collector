from django.shortcuts import render

# Add the following import
from django.http import HttpResponse

from .models import Snippet


# Define the home view
def home(request):
    return render(request, 'index.html')

def snippet_index(request):
    snippet = Snippet.objects.all()
    return render(request, 'snippets/snippets.html', {'snippets': snippet})

def snippet_detail(request, snippet_id):
    snippets = Snippet.objects.get(id=snippet_id)
    return render(request, 'snippets/detail.html', {'snippets': snippets} )

def login(request):
    return render(request, 'login.html')
