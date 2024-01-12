from django.urls import path
from django.views.generic import RedirectView

from todo import views

urlpatterns = [
    path("home/", views.home),

    path("register/", views.register, name='user-registration'),
    path("login/", views.user_login, name='user-login'),
    path("logout/", views.user_logout, name ='user-logout'),

    path("tasks/create/", views.create_task, name='create-task'),
    path("tasks/", views.task_list, name='view-tasks'),
    path("tasks/update/<str:pk>/", views.update_task, name='update-task'),
    path("tasks/delete/<str:pk>/", views.delete_task, name="delete-task"),

    path("", RedirectView.as_view(url="home/"))
]
