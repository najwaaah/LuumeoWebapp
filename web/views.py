import json
from django.shortcuts import render
from .models import *

from .forms import *
from django.http import HttpResponse

# Create your views here.

def index(request):
    course = Course.objects.all()

    context = { 
      'course' : course      
        }
    return render (request, 'web/index.html', context)


def about(request):
    ratings = Rating.objects.all()

    context = { 
      'rating' : ratings       
        }
    return render (request, 'web/about.html' , context)

def courses(request):
    course = Course.objects.all()

    context = { 
      'course' : course      
        }
    return render (request, 'web/courses.html' , context)

def contact(request):
    return render(request, "web/contact.html")