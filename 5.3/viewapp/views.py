# 5.3FBV와 CBV: 언제 어떤 것을 사용해야 할까?(Function Based View)
# from django.http import HttpResponse
# from rest_framework.decorators import api_view

# @api_view(['GET', 'POST'])
# def Animal(request):
#     if request.method == 'POST':
#         return HttpResponse("Post method")
#     else:
#         return HttpResponse("Get method")

#FBV와 CBV: 언제 어떤 것을 사용해야 할까?(Class Based View)

from django.http import HttpResponse
from django.views import View

class Animal(View):
    def get(self, request):
        return HttpResponse("Get method")

    def post(self, request):
        return HttpResponse("Post method")

from rest_framework.decorators import api_view

from rest_framework.response import Response
from rest_framework import status