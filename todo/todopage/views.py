from django.shortcuts import render
from todopage.models import TodoList

# Create your views here.
def index(request):
    todos = TodoList.objects.all()
