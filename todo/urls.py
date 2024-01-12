from django.urls import path
from django.views.generic import RedirectView

from todo import views

urlpatterns = [
    path("register/", views.register),
    path("login/", views.login),
    path("home/", views.home),

    path("tasks/create/", views.create_task, name='create-task'),
    path("tasks/", views.task_list, name='view-tasks'),
    path("tasks/update/<str:pk>/", views.update_task, name='update-task'),

    path("", RedirectView.as_view(url="home/"))
]
