from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView

router = DefaultRouter()

urlpatterns=[
    # 회원가입
    path('register/', RegisterAPIView.as_view() , name='register'),
    # 로그인
    path("login/", LoginView.as_view(), name='login'),
    # 로그아웃
    path("logout/", LogoutView.as_view(), name='logout'),
    path("auth/refresh/", TokenRefreshView.as_view()), # jwt 토큰 재발급
]