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
    path('poodles/<int:poodle_id>/add_feeding/', views.add_feeding, name='add_feeding'),
    path('toys/', views.ToyList.as_view(), name='toys_index'),
    path('toys/<int:pk>/', views.ToyDetail.as_view(), name='toys_detail'),
    path('toys/create/', views.ToyCreate.as_view(), name='toys_create'),
    path('toys/<int:pk>/update/', views.ToyUpdate.as_view(), name='toys_update'),
    path('toys/<int:pk>/delete/', views.ToyDelete.as_view(), name='toys_delete'),
    path('poodles/<int:poodle_id>/assoc_toy/<int:toy_id>/', views.assoc_toy, name='assoc_toy'),
]