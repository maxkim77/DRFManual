from django.urls import include, path

urlpatterns = [
    path('', include('myapp.urls')),
    # 다른 URL 패턴들...
]
