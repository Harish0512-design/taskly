# from django.http import HttpResponse
from django.shortcuts import render
from django.db import connection
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

    # queryset : set of objects in db

    # <QuerySet [<Task: Complete Django- # 1>, <Task: Environments- # 2>, <Task: Docker- # 3>, <Task: Kubernates- # 4>, <Task: Django Rest Framework- # 5>, <Task: Jwt Token- # 6>]>

    # single_task_obj = Task.objects.get(id=3)
    # <Task: Docker- # 3>

    # __contains like this : called as FieldLookups

    # filtered_queryset = Task.objects.filter(content__contains = "Django")
    # filtered_queryset = Task.objects.filter(content__icontains = "Django")

    # filtered_queryset = Task.objects.filter(content__startswith = "Django")
    # filtered_queryset = Task.objects.filter(content__istartswith = "Django")

    # filtered_queryset = Task.objects.filter(content__endswith = "Django")
    # filtered_queryset = Task.objects.filter(content__iendswith = "Django")

    # filtered_queryset = Task.objects.filter(id__in=[3,4,5])

    # filtered_queryset = Task.objects.filter(id__gt = 2)
    # filtered_queryset = Task.objects.filter(id__gte = 2)

    # filtered_queryset = Task.objects.filter(id__lt = 2)
    # filtered_queryset = Task.objects.filter(id__lte = 2)

    # filtered_queryset = Review.objects.filter(date_posted__isnull=True)

    # filtered_queryset = Task.objects.filter(date_posted__year = 2024)
    # filtered_queryset = Task.objects.filter(date_posted__month = 1)
    # filtered_queryset = Task.objects.filter(date_posted__day = 11)

    # filtered_queryset = Task.objects.filter(date_posted__date = datetime.date(2024, 1, 11))
    # filtered_queryset = Task.objects.filter(date_posted__date_gt = datetime.date(2024, 1, 11))

    # filtered_queryset = Task.objects.filter(date_posted__hour = 3)
    # filtered_queryset = Task.objects.filter(date_posted__minute = 3)
    # filtered_queryset = Task.objects.filter(date_posted__second = 3)


    # FieldLookUps on single object

    # queryset_obj = Task.objects.get(id__exact=14)
    # queryset_obj = Task.objects.get(title__iexact="Django")

    # queryset_obj = Review.objects.get(task__title__contains = "Django")


    # queryset_obj = Task.objects.get(title__regex=r'^(An?|The) +')
    # queryset_obj = Task.objects.get(title__iregex=r'^(An?|The) +')

    # Note:

    # query_obj_address = single_task_obj.query (or) tasks_queryset.query
    # sql_limit_time = connection.queries
    # o/p: [{'sql': 'SELECT "todo_task"."id", "todo_task"."date_updated", "todo_task"."title", "todo_task"."content", "todo_task"."date_posted" FROM "todo_task" WHERE "todo_task"."id" = 2 LIMIT 21', 'time': '0.016'}]

    context = {
        "tasks": tasks_queryset
    }

    return render(request, "todo/index.html", context=context)
