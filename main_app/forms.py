from django.forms import ModelForm
from .models import Maintaining

class MaintainingForm(ModelForm):
  class Meta:
    model = Maintaining
    fields = ['date', 'method']