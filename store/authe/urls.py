from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

from . import views

app_name = 'authe'

urlpatterns = [
    path('', views.UserViewSet.as_view({'get': 'retrieve', 'post': 'create'}), name='user_register'),
    path('login/', TokenObtainPairView.as_view(), name='user_login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('admin/<int:pk>/', views.RetrieveDestroyUserAPIView.as_view(), name='retrieve_update_destroy_user'),
    path('admin/', views.ListUserAPIView.as_view(), name='list_user'),
]