from django.shortcuts import render
from .models import Poodle
from django.http import HttpResponse


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