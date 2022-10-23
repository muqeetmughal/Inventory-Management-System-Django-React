from django.urls import path

from .views import MyTokenObtainPairView, CustomTokenRefreshView
urlpatterns = [

    path('login', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh', CustomTokenRefreshView.as_view(), name='token_refresh'),
    
    
]
