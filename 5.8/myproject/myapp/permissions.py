from rest_framework import permissions

class CustomPermission(permissions.BasePermission):
    """
    사용자 정의 권한.
    사용자의 username이 'admin'인 경우에만 접근을 허용합니다.
    """

    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.username == 'admin'
