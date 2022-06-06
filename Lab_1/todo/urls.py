from django.urls import path
from .views import index, get_task, delete_task, finish_task, edit_task, add_task

app_name = 'todo'

urlpatterns = [
    path('', index, name='index'),
    path('task/<int:task_id>', get_task, name='task_details'),
    path('task/finish/<int:task_id>', finish_task, name='task_finished'),
    path('task/edit/<int:task_id>', edit_task, name='task_edit'),
    path('task/delete/<int:task_id>', delete_task, name='task_delete'),
    path('task/add/', add_task, name='task_add'),

]
