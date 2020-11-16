      {% if cat.age > 0 %}
        <p>Age: {{ cat.age }}</p>
      {% else %}
        <p>Age: Kitten</p>
      {% endif %}


from the views page, the original index list for all the snippets:

def snippet_index(request):
    snippet = Snippet.objects.all()
    return render(request, 'snippets/snippets.html', {'snippets': snippet})


  @login_required
def add_usage(request, snippet_id):
  snippet = Snippet.objects.get(id=snippet_id)
  # instantiate FeedingForm to be rendered in the template
  usage_form = UsageForm()
  return render(request, 'snippets/detail.html', {
    # include the cat and feeding_form in the context
    'snippet': snippet, 'usage_form': usage_form
  })

    


    max_length=1,
    # add the 'choices' field option
    choices=PROJECTS,
    # set the default value for meal to be 'B'
    default=PROJECTS[0][0]