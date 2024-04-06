from django.urls import path, include
from . import views

app_name = 'brain'

urlpatterns = [
    path('', views.task_view, name='task_view'),
    path('create/', views.task_create, name='task_create'),
    path('task/<int:pk>/delete/', views.delete_task, name='delete_task'),
    path('task/<int:pk>/update/', views.task_update, name='task_update'),
]