# from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.db import connection

from .forms import TaskForm
from .models import Task


# Create your views here.
def register(request):
    # return HttpResponse("Registration page")
    return render(request, "todo/register.html")


def login(request):
    users_details = [
        {
            "id": 1,
            "name": "Harish",
            "Profession": "Software Engineer"
        },
        {
            "id": 2,
            "name": "Harish2",
            "Profession": "Software Engineer"
        },
        {
            "id": 3,
            "name": "Harish3",
            "Profession": "Software Engineer"
        }
    ]

    context = {"users": users_details}

    # return HttpResponse("Login page")
    return render(request, "todo/login.html", context=context)


def home(request):
    tasks_queryset = Task.objects.all()

    context = {
        "tasks": tasks_queryset
    }

    return render(request, "todo/index.html", context=context)


def create_task(request):
    form = TaskForm()
    success_msg = "Task Created Successfully"
    error_msg = "Something Went Wrong. Please Try Again..."

    if request.method == "POST":
        form = TaskForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("/todo/create-task/?msg=" + success_msg)

        return redirect("/todo/create-task/?msg=" + error_msg)

    context = {'form': form}

    return render(request, "todo/task_form.html", context=context)


def task_list(request):
    tasks = Task.objects.all()
    context = {"tasks": tasks}

    return render(request, "todo/task_list.html", context=context)
