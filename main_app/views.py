from django.shortcuts import render, redirect
from .models import Poodle, Toy
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .forms import FeedingForm

class PoodleCreate(CreateView):
  model = Poodle
  fields = ['name', 'description', 'age']
  success_url = '/poodles/'

class PoodleUpdate(UpdateView):
  model = Poodle
  # Let's disallow the renaming of a cat by excluding the name field!
  fields = ['description', 'age']

class PoodleDelete(DeleteView):
  model = Poodle
  success_url = '/poodles/'

class ToyList(ListView):
  model = Toy

class ToyDetail(DetailView):
  model = Toy

class ToyCreate(CreateView):
  model = Toy
  fields = '__all__'

class ToyUpdate(UpdateView):
  model = Toy
  fields = ['name', 'color']

class ToyDelete(DeleteView):
  model = Toy
  success_url = '/toys/'

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
  feeding_form = FeedingForm()
  id_list = poodle.toys.all().values_list('id')
  toys_poodle_doesnt_have = Toy.objects.exclude(id__in=id_list)
  return render(request, 'poodles/detail.html', { 'poodle': poodle, 'feeding_form': feeding_form, 'toys': toys_poodle_doesnt_have })

def add_feeding(request, poodle_id):
  # create a ModelForm instance using the data in request.POST
  form = FeedingForm(request.POST)
  # validate the form
  if form.is_valid():
    # don't save the form to the db until it
    # has the cat_id assigned
    new_feeding = form.save(commit=False)
    new_feeding.poodle_id = poodle_id
    new_feeding.save()
  return redirect('detail', poodle_id=poodle_id)

def assoc_toy(request, poodle_id, toy_id):
  # Note that you can pass a toy's id instead of the whole toy object
  Poodle.objects.get(id=poodle_id).toys.add(toy_id)
  return redirect('detail', poodle_id=poodle_id)