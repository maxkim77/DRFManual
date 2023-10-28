from django.urls import path
from . import views

urlpatterns = [
    path('animals/', views.AnimalList.as_view()),
    path('animals/<int:pk>/', views.AnimalDetail.as_view()),
]
