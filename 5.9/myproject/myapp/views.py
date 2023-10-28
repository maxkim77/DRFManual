# views.py 파일

from rest_framework import generics
from .models import Animal
from .serializers import AnimalSerializer
from .pagination import CustomPagination

class AnimalListView(generics.ListAPIView):
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer
    pagination_class = CustomPagination
    # 필요한 경우 여기에 filter_backends 및 기타 설정 추가


# # views.py

# from rest_framework import generics
# from .models import Animal
# from .serializers import AnimalSerializer
# from django_filters.rest_framework import DjangoFilterBackend
# from rest_framework.filters import SearchFilter, OrderingFilter

# class AnimalListView(generics.ListAPIView):
#     queryset = Animal.objects.all()
#     serializer_class = AnimalSerializer
#     filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
#     filterset_fields = ['name', 'species']
#     search_fields = ['name', 'species']
#     ordering_fields = ['name', 'species']
