from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('notice', views.notice, name='notice'),
]