from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import register_user
from django.urls import path

urlpatterns = [
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
    path('register/', register_user)
]