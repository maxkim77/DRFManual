from django.urls import path
from myapp import views

urlpatterns = [
    path('animals/<int:pk>/', views.AnimalDetailView.as_view(), name='animal-detail'),
    path('animals/add/', views.AnimalAddView.as_view(), name='animal-add'),
]
