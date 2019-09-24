from django.urls import path
from todopage import views

urlpatterns = [
    path('', views.index, name="TodoList")
]
