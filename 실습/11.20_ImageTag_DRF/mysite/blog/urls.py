from django.urls import include, path
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('post', views.PostViewSet) # url 2개 자동 생성

urlpatterns = [
    path('', include(router.urls)),
]