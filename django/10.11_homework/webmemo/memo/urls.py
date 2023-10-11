from django.urls import path
from . import views

urlpatterns = [
  path('',views.memo,name = 'memo'),
  path('<int:pk>/',views.post, name='post'),
  path('/delete/<int:pk>', views.delete, name='delete'),
]