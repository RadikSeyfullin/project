from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="TodoList"),
    path('addTodo/', views.addTodo, name="addTodo"),
    path('deleteTodo/<int:todo_id>/', views.deleteTodo, name="deleteTodo"),
    path('completeTodo/<int:todo_id>', views.completeTodo, name="completeTodo"),
    path('notcompleteTodo/<int:todo_id>', views.notcompleteTodo, name="notcompleteTodo"),
]
