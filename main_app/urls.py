from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('poodles/', views.poodles_index, name='index'),
    path('poodles/<int:poodle_id>/', views.poodles_detail, name='detail'),
]