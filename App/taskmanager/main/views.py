from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm


def index(request):
    tasks = Task.objects.order_by('-id')
    return render(request, 'main/index.html', {'title': 'Home page of site', 'tasks': tasks})


def about(request):
    return render(request, 'main/about.html')


def create(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            redirect('home')
        else:
            error = 'Form is not undefind'


    form = TaskForm()
    context = {
        'form': form,

    }
    return render(request, 'main/create.html', context)