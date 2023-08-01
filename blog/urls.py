from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
# router.register('board', views.BoardViewSet)

urlpatterns=[
    # 회원가입
    path('register/', RegisterAPIView.as_view() , name='register'),
]