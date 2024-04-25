from django.urls import path
from . import views

urlpatterns = [
    path('',views.todo_lists,name='todo-list'),
    path('edit/<int:pk>',views.todo_edit,name='todo-edit'),
    path('delete/<int:pk>',views.todo_delete,name='todo-delete'),
]