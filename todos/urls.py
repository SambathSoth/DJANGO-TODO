from django.urls import path
from .views import (
    todo_list_view,
    insert_todo_view,
    delete_todo_view,
)

app_name = 'todos'
urlpatterns = [
    path('list/', todo_list_view, name='todo-list'),
    path('insert/', insert_todo_view, name='todo-insert'),
    path('delete/<int:id>', delete_todo_view, name='todo-delete'),
]
