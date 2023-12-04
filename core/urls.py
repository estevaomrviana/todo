from django.urls import path 
from . import views

# app_name = 'core'

urlpatterns = [
    path('', views.index, name='home'),
    path('register', views.register, name='register'),
]

htmxpatterns = [
    path('create_todo/', views.create_todo, name='create_todo'),
    path('delete_todo/<int:pk>/', views.delete_todo, name='delete_todo'),
    path('mark_todo/<int:pk>/', views.mark_todo, name='mark_todo'),
]

urlpatterns += htmxpatterns