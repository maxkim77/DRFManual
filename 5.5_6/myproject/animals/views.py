# 5.5 APIView 클래스의 활용
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from .models import Animal
# from .serializers import AnimalSerializer

# class AnimalList(APIView):
#     def get(self, request, format=None):
#         animals = Animal.objects.all()
#         serializer = AnimalSerializer(animals, many=True)
#         return Response(serializer.data)

#     def post(self, request, format=None):
#         serializer = AnimalSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# 5.5 Generic View 클래스 활용
# from rest_framework import generics
# from .serializers import AnimalSerializer
# from .models import Animal

# class AnimalList(generics.ListCreateAPIView):
#     queryset = Animal.objects.all()
#     serializer_class = AnimalSerializer
    
# class AnimalDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Animal.objects.all()
#     serializer_class = AnimalSerializer

# 5.6 Viewset 기본구조
# from rest_framework import viewsets
# from .serializers import AnimalSerializer
# from .models import Animal

# class AnimalViewSet(viewsets.ModelViewSet):
#     queryset = Animal.objects.all()
#     serializer_class = AnimalSerializer

# 5.6 Viewset 특정 조건 필터링 기능 추가
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .serializers import AnimalSerializer
from .models import Animal
from rest_framework.generics import get_object_or_404

class AnimalViewSet(viewsets.ModelViewSet):
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer

    # 기본적인 list(), create(), retrieve(), update(), partial_update(), destroy() 메서드는
    # ModelViewSet에 이미 구현되어 있습니다.

    # 추가적인 커스텀 액션을 정의하고 싶다면 @action 데코레이터를 사용할 수 있습니다.
    # 예: 특정 조건에 맞는 동물만 필터링
    @action(detail=False, methods=['get'])
    def some_custom_action(self, request):
        # 여기에 커스텀 액션 로직을 구현
        pass
