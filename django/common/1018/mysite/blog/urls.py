from django.urls import path
from . import views

urlpatterns = [
    path('', views.postlist, name='postlist'),
    path('csrf/', views.csrf, name='csrf'),
]
