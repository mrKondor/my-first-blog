from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
  #quitando esto se puede ver
    path('post/<int:pk>)/', views.post_detail, name='post_detail'),
]