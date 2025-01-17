from django.contrib import admin
from django.urls import path, include
from .import views

urlpatterns = [
    path('',views.index ,name = 'index'),
    path('about/',views.about ,name = 'about'),
    path('courses/',views.courses ,name = 'courses'),
    path('contact/',views.contact ,name = 'contact')
]