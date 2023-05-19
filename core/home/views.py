from django.shortcuts import render

# Create your views here.
# homepage
def index(request):
    return render(request, "home_index.html")
