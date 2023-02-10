from django.shortcuts import render,redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from.models import Art, Frame
from .forms import MaintainingForm

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
  id_list = art.frames.all().values_list('id')
  frames_art_doesnt_have = Frame.objects.exclude(id__in=id_list)
  maintaining_form = MaintainingForm()
  return render(request, 'arts/detail.html', { 'art': art, 'maintaining_form':maintaining_form, 'frames': frames_art_doesnt_have })


class ArtCreate(CreateView):
  model = Art
  fields = '__all__'


class ArtUpdate(UpdateView):
  model = Art
  fields = ['painting_by', 'description', 'medium']

class ArtDelete(DeleteView):
  model = Art
  success_url = '/arts'

def add_maintaining(request, art_id):
  form = MaintainingForm(request.POST)
  if form.is_valid():
    # false cunku henuz yiklenmesini istemiyoruz
    new_maintaining = form.save(commit=False)

    # asagida manupilating the data in model
    new_maintaining.art_id = art_id
    # ondan sonra kaydediyoruz
    new_maintaining.save()
  return redirect('detail', art_id=art_id)

class FrameList(ListView):
  model = Frame

class FrameDetail(DetailView):
  model = Frame

class FrameCreate(CreateView):
  model = Frame
  fields = '__all__'

class FrameUpdate(UpdateView):
  model = Frame
  fields = ['name', 'color']

class FrameDelete(DeleteView):
  model = Frame
  success_url = '/frames'


def assoc_frame(request, art_id, frame_id):
  # Note that you can pass a frame's id instead of the whole frame object
  Art.objects.get(id=art_id).frames.add(frame_id)
  return redirect('detail', art_id=art_id)

def unassoc_frame(request, art_id, frame_id):
  Art.objects.get(id=art_id).frames.remove(frame_id)
  return redirect('detail', art_id=art_id)