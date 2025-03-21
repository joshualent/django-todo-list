from django.urls import path

from .views import TodoListView, TodoDetailView

app_name = "todos"
urlpatterns = [
    path("", TodoListView.as_view(), name="todo_list"),
    path("<int:pk>/", TodoDetailView.as_view(), name="todo_detail"),
]
