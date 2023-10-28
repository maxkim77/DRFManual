from django.urls import path
from .views import AnimalAuthenticatedView

urlpatterns = [
    path('myview/', AnimalAuthenticatedView.as_view(), name='my-authenticated-view'),
]

# from django.urls import path
# from .views import AnimalCustomPermissionView

# urlpatterns = [
#     path('custom-permission/', AnimalCustomPermissionView.as_view(), name='custom-permission-view'),
# ]
