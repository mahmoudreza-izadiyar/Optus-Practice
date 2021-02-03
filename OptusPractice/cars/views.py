from django.shortcuts import render


# Create your views here.
def index(request):
    context = {
        "data": "Hello lord Mahmoud"
    }
    return render(request, "cars/index.html", context)
