from django.urls import path
from .views import *

urlpatterns = [
    path('',ReadTodo.as_view()),
    path('<int:pk>/',ReadTodo.as_view()),
    path('create',CreateTodo.as_view()),
    path('update/<int:pk>/',UpdateTodo.as_view()),
    path('delete/<int:pk>/',Deletetodo.as_view()),
]
