from django.shortcuts import render
from .models import Animal


# list of all registered animals
def index(request):
    animals = Animal.objects.all() # all registered animals
    context = {"animals": animals} # variables sent to the view
    return render(request, "animals_index.html", context)


def detail(request):
    return render(request, "detail.html")