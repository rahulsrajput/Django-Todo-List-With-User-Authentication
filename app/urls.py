from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from todo_list import settings
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

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
