from django.forms import ModelForm
from .models import UsageCounter

class UsageForm(ModelForm):
  class Meta:
    model = UsageCounter
    fields = ['date', 'type']
