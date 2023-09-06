from django.urls import path
from .views import index, create, read, delete, update


urlpatterns = [
    path('', index),
    path('create/', create),
    path('<int:todo_id>/', read),
    path('delete/<int:todo_id>/', delete),
    path('update/<int:todo_id>/', update),
]
