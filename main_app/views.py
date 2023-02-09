from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from.models import Art

arts = [
  {'name': 'Mona Lisa', 'painting_by': 'Leonardo da Vinci', 'description': 'The most parodied work of art in the world', 'medium': 'Oil paint'},
  {'name': 'The Starry Night', 'painting_by': 'Vincent van Gogh', 'description': 'The Starry Night is an oil-on-canvas painting by the Dutch Post-Impressionist painter Vincent van Gogh.', 'medium': 'Oil paint'},
]

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def arts_index(request):
  arts = Art.objects.all()
  return render(request, 'arts/index.html', {'arts': arts})

def arts_detail(request, art_id):
  art = Art.objects.get(id=art_id)
  return render(request, 'arts/detail.html', { 'art': art })


class ArtCreate(CreateView):
  model = Art
  fields = '__all__'


class ArtUpdate(UpdateView):
  model = Art
  fields = ['painting_by', 'description', 'medium']

class ArtDelete(DeleteView):
  model = Art
  success_url = '/arts'