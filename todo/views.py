from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def register(request):
    # return HttpResponse("Registration page")
    return render(request, "todo/register.html")


def login(request):
    # return HttpResponse("Login page")
    return render(request, "todo/login.html")


def home(request):
    return render(request, "todo/index.html")
