from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('poodles/', views.poodles_index, name='index'),
    path('poodles/<int:poodle_id>/', views.poodles_detail, name='detail'),
    path('poodles/create/', views.PoodleCreate.as_view(), name='poodles_create'),
    path('poodles/<int:pk>/update/', views.PoodleUpdate.as_view(), name='poodles_update'),
    path('poodles/<int:pk>/delete/', views.PoodleDelete.as_view(), name='poodles_delete'),
]