from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.view_login, name='login'),
    path('register/', views.register, name='register'),
    path('userpage/', views.userpage, name='userpage'),
    path('logout/', views.view_logout, name='logout'),
]