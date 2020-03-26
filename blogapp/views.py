from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import *


def index(request):
    context = {
        'messages': User.objects.all()
    }
    return render(request, 'index.html', context)