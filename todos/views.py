from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Todo


# Create your views here.
class TodoListView(ListView):
    model = Todo
    template_name = "todo_list.html"


class TodoDetailView(DetailView):
    model = Todo
    template_name = "todo_detail.html"
