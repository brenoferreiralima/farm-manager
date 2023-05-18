"""" home urls """
from django.urls import path
from . import views


APP_NAME = 'home'
urlpatterns = [
    path('', views.index, name='index'),
]
