from django.http import HttpResponse, Http404
from django.shortcuts import render
from .models import Home

# Create your views here.


def home(request):
    home = Home.objects.get(id=1)
    return render(request, 'home.html', {'home': home})
