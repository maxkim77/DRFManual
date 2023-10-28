from django.urls import path
from . import views

urlpatterns = [
    path('animal/', views.Animal, name='animal'),
]
