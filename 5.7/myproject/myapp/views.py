# from rest_framework import mixins, generics
# from .models import Animal
# from .serializers import AnimalSerializer

# class AnimalList(mixins.ListModelMixin,
#                  mixins.CreateModelMixin,
#                  generics.GenericAPIView):
#     queryset = Animal.objects.all()
#     serializer_class = AnimalSerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)

# class AnimalDetail(mixins.RetrieveModelMixin,
#                    mixins.UpdateModelMixin,
#                    mixins.DestroyModelMixin,
#                    generics.GenericAPIView):
#     queryset = Animal.objects.all()
#     serializer_class = AnimalSerializer

#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)

#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)

#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)

# myapp/views.py
from rest_framework import generics, mixins
from .models import Animal
from .serializers import AnimalSerializer

class LoggingMixin:
    def log_action(self, action, request):
        print(f"Action: {action}, Path: {request.path}")

class AnimalList(LoggingMixin, mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer

    def get(self, request, *args, **kwargs):
        self.log_action("List Animals", request)
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.log_action("Create Animal", request)
        return self.create(request, *args, **kwargs)

class AnimalDetail(LoggingMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer

    def get(self, request, *args, **kwargs):
        self.log_action("Retrieve Animal", request)
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        self.log_action("Update Animal", request)
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        self.log_action("Delete Animal", request)
        return self.destroy(request, *args, **kwargs)
