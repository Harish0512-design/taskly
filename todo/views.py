# from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import TaskForm, UserRegistrationForm
from .models import Task


# Create your views here.
def register(request):
    form = UserRegistrationForm()

    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()

            messages.success(request, "User Created Successfully..")
            return redirect("/todo/register")

        messages.error(request, form.errors)
        return redirect("/todo/register")

    context = {"form": form}
    return render(request, "todo/register.html", context=context)


def user_login(request):
    # return HttpResponse("Login page")

    form = AuthenticationForm()

    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")

            user = authenticate(request, username=username, password=password)
            print(user)

            if user is not None:
                login(request, user)
                messages.success(request, f"Welcome {username}..")
                return redirect("/todo/home")

            else:
                messages.error(request, f"{username} doesn't exists")
                return redirect("/todo/login")

    context = {
        "form": form
    }
    return render(request, "todo/login.html", context=context)


def home(request):
    tasks_queryset = Task.objects.all()

    context = {
        "tasks": tasks_queryset
    }
    return render(request, "todo/index.html", context=context)


def user_logout(request):
    logout(request)
    messages.success(request, "Logged Out Successfully")
    return redirect("/todo/home")


def create_task(request):
    form = TaskForm()
    success_msg = "Task Created Successfully"
    error_msg = "Something Went Wrong. Please Try Again..."

    if request.method == "POST":
        form = TaskForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("/todo/tasks/create/?msg=" + success_msg)

        return redirect("/todo/tasks/create/?msg=" + error_msg)

    context = {'form': form}

    return render(request, "todo/task_form.html", context=context)


def task_list(request):
    tasks = Task.objects.all()
    context = {"tasks": tasks}

    return render(request, "todo/task_list.html", context=context)


def update_task(request, pk):
    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)

    success_msg = "Task Updated Successfully"
    error_msg = "Something went wrong. Please Try Again..."

    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()

            messages.success(request, success_msg)
            return redirect("/todo/tasks/update/" + str(task.id))

        messages.error(request, error_msg)
        return redirect("/todo/tasks/update/" + str(task.id))

    context = {'form': form}

    return render(request, "todo/update_task.html", context=context)


def delete_task(request, pk):
    task = Task.objects.get(id=pk)

    if request.method == "POST":
        task.delete()
        messages.success(request, "Task Deleted Successfully...")
        return redirect(to="/todo/tasks/")

    context = {"object": task}

    return render(request, "todo/task_delete.html", context=context)
