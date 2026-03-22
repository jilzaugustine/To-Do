from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import task

# Create your views here.
def addTask(request):
    task_name=request.POST['task']
    task.objects.create(task=task_name)
    return redirect('home')