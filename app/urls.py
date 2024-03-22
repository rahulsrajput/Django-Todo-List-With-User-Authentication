from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginUser, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.registerUser, name='register'),

    path('', views.task_list, name='home'),
    path('add/', views.task_add, name='add'),
    path('update/<int:pk>', views.task_update, name='update'),
    path('delete/<int:pk>', views.task_delete, name='delete'),
]
