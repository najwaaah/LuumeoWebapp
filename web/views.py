from django.http import JsonResponse
from django.shortcuts import render

from web.forms import ContactForm

from .models import Course
from .models import Rating

# Create your views here.


def index(request):
    course = Course.objects.all()

    context = {"course": course,"is_home":True}
    return render(request, "web/index.html", context)


def about(request):
    ratings = Rating.objects.all()

    context = {"rating": ratings,"is_about":True}
    return render(request, "web/about.html", context)


def courses(request):
    course = Course.objects.all()

    context = {"course": course,"is_course":True}
    return render(request, "web/courses.html", context)

def contact(request):
    form = ContactForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            # Perform any necessary actions, such as saving form data
            form.save()

            # Send a success JSON response
            return JsonResponse({
                'success': True,
                'message': 'Thank you for contacting us. We will get back to you soon!'
            })

        else:
            # Send an error JSON response if the form is invalid
            return JsonResponse({
                'success': False,
                'errors': form.errors
            })

    # For GET requests, render the contact form
    context = {
        "is_contact": True,
        'form': form
    }
    return render(request, "web/contact.html", context)

