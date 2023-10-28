from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound, PermissionDenied, ValidationError
from .models import Animal

# Animal 상세 정보를 반환하는 API
class AnimalDetailView(APIView):
    def get(self, request, pk):
        try:
            animal = Animal.objects.get(pk=pk)
        except Animal.DoesNotExist:
            raise NotFound(detail="Animal not found.")

        return Response({
            "name": animal.name,
            "species": animal.species,
            "age": animal.age
        })

# Animal 추가하는 API
class AnimalAddView(APIView):
    def post(self, request):
        if not request.user.is_authenticated:
            raise PermissionDenied(detail="Authentication required.")

        name = request.data.get('name')
        species = request.data.get('species')
        age = request.data.get('age')

        if not all([name, species, age]):
            raise ValidationError("All fields 'name', 'species', and 'age' are required.")

        animal = Animal.objects.create(name=name, species=species, age=age)
        return Response({
            "id": animal.id,
            "name": animal.name,
            "species": animal.species,
            "age": animal.age
        })
