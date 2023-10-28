#5.5 실습1
# from django.urls import path
# from .views import AnimalList

# urlpatterns = [
#     path('animals/', AnimalList.as_view(), name='animal-list'),
#     path('animals/<int:pk>/', AnimalDetail.as_view(), name='animal-detail'),
# ]

#5.5 실습2
# from django.urls import path
# from .views import AnimalList, AnimalDetail

# urlpatterns = [
#     path('animals/', AnimalList.as_view(), name='animal-list'),
#     path('animals/<int:pk>/', AnimalDetail.as_view(), name='animal-detail'),
# ]

#5.6 실습3
# from rest_framework.routers import DefaultRouter
# from .views import AnimalViewSet

# router = DefaultRouter()
# router.register(r'animals', AnimalViewSet)

# urlpatterns = [

# ]

# urlpatterns += router.urls

#5.6 실습4
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AnimalViewSet

router = DefaultRouter()
router.register(r'animals', AnimalViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
