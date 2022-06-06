import random

from django.shortcuts import render, HttpResponse, redirect, reverse
from django.http.response import JsonResponse
from pprint import pprint
from .forms import TodoForm

todo_list = [
    {'id': 1, 'name': 'breakfast', 'description': 'bla bla bla', 'is_done': False},
    {'id': 2, 'name': 'lecture', 'description': 'bla bla bla', 'is_done': True},
    {'id': 3, 'name': 'lab', 'description': 'bla bla bla', 'is_done': False}
]


def index(request, **kwargs):
    return render(request, 'todo/index.html', context={'list': todo_list, 'title': "Todo Tasks"})


def get_task(request, **kwargs):
    task = {}
    for item in todo_list:
        if item.get('id') == kwargs.get('task_id'):
            task = item
            # task = todo_list[todo_list.index(item)]
    print(f'Task: {task}')
    return render(request, 'todo/task_details.html', context={'task': task, 'title': 'Task Details'})


def add_task(request, **kwargs):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            print(form.data)
            todo_list.append({
                "id": random.randint(1, 999),
                "name": form.data.get('name'),
                "description": form.data.get('description'),
                "is_done": False,
            })
        return redirect(reverse('todo:index'))
    form = TodoForm()
    return render(request, "todo/task_form.html", {"form": form, "title": "Add new Task"})


def edit_task(request, **kwargs):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            for item in todo_list:
                if item.get('id') == kwargs.get('task_id'):
                    item.update({
                        "name": form.data.get('name'),
                        "description": form.data.get('description')
                    })
        return redirect(reverse('todo:index'))
    task = {}
    for item in todo_list:
        if item.get('id') == kwargs.get('task_id'):
            task = item
    # todo = list(filter(lambda n: n['id'] == kwargs.get('todo_id'), todos))[0]
    form = TodoForm(task)
    return render(request, "todo/task_form.html", {"form": form, "title": "Edit Task"})


def finish_task(request, **kwargs):
    for item in todo_list:
        if item.get('id') == kwargs.get('task_id'):
            item['is_done'] = True
    return redirect(reverse('todo:index'))


def delete_task(request, **kwargs):
    for item in todo_list:
        if item.get('id') == kwargs.get('task_id'):
            todo_list.remove(item)
            # todo_list.pop(todo_list.index(item))
    return redirect(reverse('todo:index'))
    # return render(request, 'todo/index.html', context={'list': todo_list})
