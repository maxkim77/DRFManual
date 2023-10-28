from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

class AnimalAuthenticatedView(APIView):
    permission_classes = [IsAuthenticated]

    def Animal(self, request):
        content = {'message': '이 메시지는 인증된 사용자만 볼 수 있습니다.'}
        return Response(content)

# from rest_framework.views import APIView
# from rest_framework.response import Response
# from .permissions import CustomPermission

# class AnimalCustomPermissionView(APIView):
#     permission_classes = [CustomPermission]

#     def Animal(self, request):
#         content = {'message': '사용자 정의 권한을 통과한 사용자만 이 메시지를 볼 수 있습니다.'}
#         return Response(content)
