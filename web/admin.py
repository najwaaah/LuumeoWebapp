from django.contrib import admin
from .models import Contact, Course, Rating

# Register your models here.
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone')

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ( 'name',)     

@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ( 'name',)  