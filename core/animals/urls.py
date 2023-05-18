""" animals urls """
from django.urls import path
from . import views


APP_NAME = "animals"
urlpatterns = [
    path("", views.index, name="index"),
    path("detail/", views.detail, name="detail"),
]
