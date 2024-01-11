from django.urls import path
from django.views.generic import RedirectView

from todo import views

urlpatterns = [
    path("register/", views.register),
    path("login/", views.login),
    path("home/", views.home),
    path("create-task/", views.create_task, name='create-task'),
    path("tasks/", views.task_list, name='view-tasks'),
    path("", RedirectView.as_view(url="home/"))
]
