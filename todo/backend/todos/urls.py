# todos/urls.py
# detailTodo to view the entire model while List.todo to view only the each object
from django.urls import path
from .views import ListTodo, DetailTodo
urlpatterns = [
    path('<int:pk>/', DetailTodo.as_view()),
    path('', ListTodo.as_view()),
]