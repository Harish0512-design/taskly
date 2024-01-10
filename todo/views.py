from django.http import HttpResponse
from django.shortcuts import render


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
    context = {
        "first_name": "Harish",
        "last_name": "Somsole"
    }
    return render(request, "todo/index.html", context=context)
