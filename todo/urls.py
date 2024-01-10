from django.urls import path
from django.views.generic import RedirectView

from todo import views

urlpatterns = [
    path("register/", views.register),
    path("login/", views.login),
    path("", RedirectView.as_view(url="register/"))
]
