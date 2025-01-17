from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone = models.IntegerField()
    message = models.TextField()




    def __str__(self):
        return self.name
    
class Course(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='media/course')
    description = models.TextField()
    full_name = models.CharField(max_length=50)


    class Meta:
        verbose_name_plural = "course"
        verbose_name = "Course"
    def __str__(self):
        return self.name 

class Rating(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='media/ratings')
    description = models.TextField()
    position = models.CharField(max_length=50)


    class Meta:
        verbose_name_plural = "rating"
        verbose_name = "Ratings"
    def __str__(self):
        return self.name 