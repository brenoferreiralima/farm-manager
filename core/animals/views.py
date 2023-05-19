from django.shortcuts import render

# Create your views here.
# list of all registered animals
def index(request):
    return render(request, "animals_index.html")


def detail(request):
    return render(request, "detail.html")