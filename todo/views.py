from django.views.generic import ListView, CreateView, DeleteView
from django.urls import reverse_lazy

from .models import Todo


class TodoListView(ListView):
    model = Todo
    template_name = 'todo/todo_index.html'


class TodoCreateView(CreateView):
    model = Todo
    fields = '__all__'
    template_name = 'todo/todo_form.html'
    success_url = reverse_lazy('todo:index')


class TodoDeleteView(DeleteView):
    model = Todo
    template_name = 'todo/todo_confirm_delete.html'
    success_url = reverse_lazy('todo:index')