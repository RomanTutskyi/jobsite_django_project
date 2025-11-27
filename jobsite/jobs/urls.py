from django.urls import path
from . import views

urlpatterns = [
    path('', views.job_list, name='job_list'),
    path('jobs/<int:pk>/', views.job_detail, name='job_detail'),
    path('jobs/new/', views.job_create, name='job_create'),
    path('register/', views.register, name='register'),
]
