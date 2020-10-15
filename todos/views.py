from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from .models import Todo

# Create your views here.
def todo_list_view(request):
    todos = Todo.objects.all()
    context = {
        'todos': todos
    }
    return render(request, 'todos/todo_list.html', context)

def insert_todo_view(request:HttpRequest):
    todo = Todo(content = request.POST['content'])
    todo.save()
    return redirect('/todos/list/')

def delete_todo_view(request, id):
    todo_delete = Todo.objects.get(id=id)
    todo_delete.delete()
    return redirect('/todos/list/')
