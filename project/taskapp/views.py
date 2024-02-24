# views.py

from django.shortcuts import get_object_or_404,render, redirect
from .models import Task

def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'task_list.html', {'tasks': tasks})

def add_task(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        Task.objects.create(title=title)
        return redirect('task_list')
    return render(request, 'add_task.html')

def update_task(request, task_id):
    task = Task.objects.get(pk=task_id)

    if request.method == 'POST':
        title = request.POST.get('title')
        task.title = title
        task.save()
        return redirect('task_list')

    return render(request, 'update_task.html', {'task': task})
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    
    if request.method == 'POST':
        task.delete()
        return redirect('task_list')
    
    return render(request, 'delete_task.html', {'task': task})
