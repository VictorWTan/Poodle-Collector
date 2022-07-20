from django.shortcuts import render
from .models import Poodle
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView

class PoodleCreate(CreateView):
  model = Poodle
  fields = '__all__'
  success_url = '/poodles/'

class PoodleUpdate(UpdateView):
  model = Poodle
  # Let's disallow the renaming of a cat by excluding the name field!
  fields = ['description', 'age']

class PoodleDelete(DeleteView):
  model = Poodle
  success_url = '/poodles/'

# Define the home view
def home(request):
  return HttpResponse('<h1>Hello, welcome home.</h1>')

def about(request):
  return render(request, 'about.html')

def poodles_index(request):
  poodles = Poodle.objects.all()
  return render(request, 'poodles/index.html', { 'poodles': poodles })

def poodles_detail(request, poodle_id):
  poodle = Poodle.objects.get(id=poodle_id)
  return render(request, 'poodles/detail.html', { 'poodle': poodle })