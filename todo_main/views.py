


from django.shortcuts import render
from todo.models import task

def home(request):
    tasks=task.objects.filter(is_completed=False).order_by('-updated_at')
    print(tasks)
    completed_tasks=task.objects.filter(is_completed=True)
    print(completed_tasks)
    context={
        'tasks':tasks,
        'completed_tasks':completed_tasks
    }
    return render(request,'home.html',context)