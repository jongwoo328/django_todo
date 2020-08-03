from django.urls import path

from . import views


app_name = 'todo'

urlpatterns = [
    path('', views.TodoListView.as_view(), name='index'),
    path('create/', views.TodoCreateView.as_view(), name='create'),
    path('delete/<int:pk>/', views.TodoDeleteView.as_view(), name='delete'),
]