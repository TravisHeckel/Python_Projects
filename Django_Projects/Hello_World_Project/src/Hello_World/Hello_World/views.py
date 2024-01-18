from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    users = ["Tyler", "Edward", "Sierra", "Madison", "Josh", "Hubby", "Rebecca"]
    context = {
        'group1': users,
    }

    return render(request, "home.html", context)
