from django.urls import path
from todolist.views import finish_task
from todolist.views import show_create_task
from todolist.views import  show_todolist,register,login_user,logout_user,finish_task,delete_task
from todolist.models import TodoList

app_name = 'todolist'

urlpatterns = [
    path('', show_todolist, name='show_todolist'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('create-task/', show_create_task, name='show_create_task'),
    path('finish-task/<int:pk>', finish_task, name='finish_task'),
    path('delete-task/<int:pk>', delete_task, name='delete_task'),
]

