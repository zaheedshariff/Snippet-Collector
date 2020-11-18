from django.shortcuts import render, redirect

# Add the following import
from django.http import HttpResponse

from .models import Snippet, Use, UsageCounter
from .forms import UsageForm

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView

from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

class SnippetCreate(LoginRequiredMixin, CreateView):
    model = Snippet
    fields = ['language', 'type', 'category', 'description', 'year_discovered']
    success_url = '/snippets/'
    def form_valid(self, form):
    # Assign the logged in user (self.request.user)
        form.instance.user = self.request.user  # form.instance is the cat
    # Let the CreateView do its job as usual
        return super().form_valid(form)


class SnippetEdit(LoginRequiredMixin, UpdateView):
    model = Snippet
    fields = "__all__"


class SnippetDelete(LoginRequiredMixin, DeleteView):
    model = Snippet
    success_url = '/snippets/'

# class SnippetList(ListView):
#     snippets = Snippet.objects.filter(user=user)
#     model = Snippet

# Define the home view
def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('accounts/login.html')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

# def login(request):
#     return render(request, 'login.html')

@login_required
def snippet_index(request):
    snippets = Snippet.objects.filter(user=request.user)
    # snippet = Snippet.objects.all()
    return render(request, 'snippets/snippets.html', {'snippets': snippets})


@login_required
def snippet_detail(request, snippet_id):
    snippet = Snippet.objects.get(id=snippet_id)
    project_not_used = Use.objects.exclude(id__in = snippet.uses.all().values_list('id'))
    usage_form = UsageForm()
    return render(request, 'snippets/detail.html', {'snippet': snippet,
    'usage_form': usage_form, 'uses': project_not_used
})

@login_required
def usage_form(request, snippet_id):
  # create a ModelForm instance using the data in request.POST
  form = UsageForm(request.POST)
  # validate the form
  if form.is_valid():
    # don't save the form to the db until it
    # has the cat_id assigned
    new_usage = form.save(commit=False)
    new_usage.snippet_id = snippet_id
    new_usage.save()
  return redirect('detail', snippet_id=snippet_id)

@login_required
def assoc_project(request, snippet_id, use_id):
  # Note that you can pass a toy's id instead of the whole object
  Snippet.objects.get(id=snippet_id).uses.add(use_id)
  return redirect('detail', snippet_id=snippet_id)