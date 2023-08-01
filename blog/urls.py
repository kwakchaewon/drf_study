from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView

router = DefaultRouter()

urlpatterns=[
    path('register/', RegisterAPIView.as_view() , name='register'), # 회원가입
    path("login/", LoginView.as_view(), name='login'),  # 로그인
    path("logout/", LogoutView.as_view(), name='logout'),   # 로그아웃
    path("auth/refresh/", TokenRefreshView.as_view()),  # jwt 토큰 재발급
]