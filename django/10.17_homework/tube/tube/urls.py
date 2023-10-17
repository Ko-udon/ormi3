from django.urls import path
from . import views

urlpatterns = [
    path('', views.postlist, name='postlist'),
    path('<int:pk>/', views.postdetail, name='postdetail'),
    path('tag/<str:tag>/', views.posttag, name='posttage'),
    path('create/', views.create, name='create'),
    path('update/<int:pk>/', views.update, name='update'),
    path('delete/<int:pk>/', views.delete, name='delete'),
]