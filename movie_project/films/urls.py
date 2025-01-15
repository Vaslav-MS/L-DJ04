from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='films'),
    path('add/', views.create, name='add_films')
]
