from django.urls import path 
from . import views

# app_name = 'core'

urlpatterns = [
    path('', views.index, name='home'),
    path('projeto/<int:id>/', views.project_detail,name='project_detail'),
    path('register', views.register, name='register'),
]

htmxpatterns = [
    path('create_project/', views.create_project, name='create_project'),
    path('create_todo/', views.create_todo, name='create_todo'),
    path('delete_todo/<int:pk>/', views.delete_todo, name='delete_todo'),
    path('mark_todo/<int:pk>/', views.mark_todo, name='mark_todo'),
]

urlpatterns += htmxpatterns