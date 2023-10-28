# urls.py

from django.urls import path
from .views import AnimalListView

urlpatterns = [
    path('animals/', AnimalListView.as_view(), name='animal-list'),
]
