from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# @api_view 데코레이터를 사용하여 뷰를 정의
@api_view(['GET', 'POST'])
def Animal(request):
    # GET 요청 처리
    if request.method == 'GET':
        data = {'message': 'GET 요청을 받았습니다.'}
        return Response(data, status=status.HTTP_200_OK)
    # POST 요청 처리
    elif request.method == 'POST':
        data = {'message': 'POST 요청을 받았습니다.'}
        return Response(data, status=status.HTTP_201_CREATED)