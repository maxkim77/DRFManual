from django.urls import path
from .views import Animal

urlpatterns = [
    # path('animal/', Animal, name='animal'),  # 함수 기반 뷰
    path('animal/', Animal.as_view(), name='animal'),  # 클래스 기반 뷰
    
]
