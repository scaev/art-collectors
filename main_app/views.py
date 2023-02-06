from django.shortcuts import render

arts = [
  {'name': 'Mona Lisa', 'paintingby': 'Leonardo da Vinci', 'description': 'The most parodied work of art in the world', 'medium': 'Oil paint'},
  {'name': 'The Starry Night', 'paintingby': 'Vincent van Gogh', 'description': 'The Starry Night is an oil-on-canvas painting by the Dutch Post-Impressionist painter Vincent van Gogh.', 'medium': 'Oil paint'},
]

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def arts_index(request):
  return render(request, 'arts/index.html', {'arts': arts})