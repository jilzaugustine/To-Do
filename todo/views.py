from multiprocessing import context

from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from .models import task

# Create your views here.
def addTask(request):
    task_name=request.POST['task']
    task.objects.create(task=task_name)
    return redirect('home')
def mark_as_done(request,pk):
    task_name=get_object_or_404(task,pk=pk)
    task_name.is_completed=True
    task_name.save()

    return redirect('home')
def mark_as_undone(request,pk):
    task_name=get_object_or_404(task,pk=pk)
    task_name.is_completed=False
    task_name.save()
    return redirect("home")
def editTask(request,pk):
    get_task=get_object_or_404(task,pk=pk)
    if request.method=='POST':
        new_task=request.POST['task']
        get_task.task=new_task
        get_task.save()
        return redirect('home')

    else:
        context={
            'get_task':get_task
        }
        return render(request,'editTask.html',context)
def delete(request, pk):
    if request.method == 'POST':
        t = get_object_or_404(task, pk=pk)
        t.delete()
    return redirect('home')