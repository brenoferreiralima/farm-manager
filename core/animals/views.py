from django.shortcuts import render

# Create your views here.
# list of all registered animals
def index(request):
    return render(request, "index.html")