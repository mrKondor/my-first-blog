from django.urls import path 
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    #la linea antes de poner esta linea me salia el famoso reverseMatch en el servidor
    path('post/new', views.post_new, name='post_new'),
]