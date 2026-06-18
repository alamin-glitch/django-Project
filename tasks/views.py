from .models import Task
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm
from .forms import TaskForm
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator
from django.contrib.auth import logout


# Create your views here.



def register_view(request):

    if request.method == 'POST':

        form = RegisterForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)

            return redirect('task_list')

    else:
        form = RegisterForm()

    return render(
        request,
        'tasks/register.html',
        {'form': form}
    )

def login_view(request):

    if request.method == 'POST':

        form = AuthenticationForm(
            request,
            data=request.POST
        )

        if form.is_valid():
            user = form.get_user()
            login(request, user)

            return redirect('task_list')

    else:
        form = AuthenticationForm()

    return render(
        request,
        'tasks/login.html',
        {'form': form}
    )

def logout_view(request):

    logout(request)

    return redirect('login')

from .models import Task

@login_required
def task_list(request):

    search = request.GET.get('q')

    tasks = Task.objects.filter(owner=request.user).order_by('-created_at')

    if search:
        tasks = tasks.filter(
            title__icontains=search
        )

    paginator = Paginator(tasks, 5) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'tasks': page_obj
    }

    return render(
        request,
        'tasks/task_list.html',
        context
    )

@login_required
def task_create(request):

    if request.method == 'POST':

        form = TaskForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():

            task = form.save(commit=False)

            task.owner = request.user

            task.save()

            messages.success(
                request,
                'Task created successfully!'
            )

            return redirect('task_list')

    else:

        form = TaskForm()

    return render(
        request,
        'tasks/task_form.html',
        {'form': form}
    )
@login_required
def task_update(request, pk):

    task = get_object_or_404(
        Task,
        pk=pk,
        owner=request.user
    )

    if request.method == 'POST':

        form = TaskForm(
            request.POST,
            request.FILES,
            instance=task
        )

        if form.is_valid():

            form.save()

            messages.success(
                request,
                'Task updated successfully!'
            )

            return redirect('task_list')

    else:

        form = TaskForm(instance=task)

    return render(
        request,
        'tasks/task_form.html',
        {
            'form': form
        }
    )
@login_required
def task_delete(request, pk):

    task = get_object_or_404(
        Task,
        pk=pk,
        owner=request.user
    )

    if request.method == 'POST':

        task.delete()

        messages.success(
            request,
            'Task deleted successfully!'
        )

        return redirect('task_list')

    return render(
        request,
        'tasks/task_confirm_delete.html',
        {
            'task': task
        }
    )
def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def task_detail(request, pk):

    task = get_object_or_404(
        Task,
        pk=pk,
        owner=request.user
    )

    return render(
        request,
        'tasks/task_details.html',
        {
            'task': task
        }
    )