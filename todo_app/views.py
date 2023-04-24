from datetime import datetime

from django.shortcuts import render

from todo_app.models import TodoTask, TodoStatus, TodoList


def todo_main(request):
    if request.method == 'POST':
        type = request.POST.get('type')
        if type == 'create':
            todo = TodoTask()
            todo.title = request.POST.get('title')
            todo.status = TodoStatus.objects.get(pk=TodoStatus.C_NOT_COMPLETED)
            todo.create_at = datetime.now()
            todo.text = ''
            todo.todo_list = TodoList.objects.get(pk=1)
            todo.save()
        if type == 'destroy':
            TodoTask.objects.get(pk=request.POST.get('task_id')).delete()

    return render(request, 'todo_main.html', {
        'task_array': TodoTask.objects.all().order_by('-id')
    })
