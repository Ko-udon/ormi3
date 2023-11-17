from django.contrib import admin
from django.urls import path, include
from accounts import views

urlpatterns = [
    path('', include('dj_rest_auth.urls')),
    path('join/', include('dj_rest_auth.registration.urls')),
    path('mypage', view=views.mypage),
]