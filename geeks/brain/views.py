from django.shortcuts import render, redirect, get_object_or_404
from rest_framework import viewsets
from .models import Task
from .forms import TaskSerializer, TaskForm


def task_view(request):
    tasks = Task.objects.all()
    context = {'tasks': tasks}
    return render(request, 'brain/index.html', context)

def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('brain:task_view')
    else:
        form = TaskForm()
    return render(request, 'brain/task_form.html', {'form': form})

def task_update(request, pk):
    task = get_object_or_404(Task, pk=pk)
    form = TaskForm(request.POST or None, instance=task)
    context = {'form': form}
    if form.is_valid():
        form.save()
        return redirect('brain:task_view')
    return render(request, 'brain/task_form.html', context)

def delete_task(pk):
    task = get_object_or_404(TaskForm, pk=pk)
    task.delete()
    return redirect('brain:task_view')
