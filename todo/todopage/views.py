from django.shortcuts import render
from todopage.models import TodoList, Category
from django.http import HttpResponseRedirect

# Create your views here.
def index(request):
    not_comp_todos = TodoList.objects.filter(status=False)
    comp_todos = TodoList.objects.filter(status=True)
    categories = Category.objects.all()
    return render(request, 'index.html', {'not_comp_todos': not_comp_todos, 'comp_todos': comp_todos, 'categories': categories})

def addTodo(request):
    new_item = request.POST['add_item']
    new_cat = request.POST['add_category']
    c = Category.objects.get(title=new_cat)
    a = TodoList(title = new_item, category = c)
    a.save()
    return HttpResponseRedirect('/')

def deleteTodo(request, todo_id):
    item = TodoList.objects.get(id=todo_id)
    item.deleted = True
    item.save()
    return HttpResponseRedirect('/')

def completeTodo(request, todo_id):
    item = TodoList.objects.get(id=todo_id)
    item.status = True
    item.save()
    return HttpResponseRedirect('/')

def notcompleteTodo(request, todo_id):
    item = TodoList.objects.get(id=todo_id)
    item.status = False
    item.save()
    return HttpResponseRedirect('/')
