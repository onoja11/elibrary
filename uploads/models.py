from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class StaffWriting(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    level=models.CharField(max_length=200, default="100 Level",choices=[
        ('100 Level', "100 Level"),
        ('200 Level', "200 Level"),
        ('300 Level', "300 Level"),
         ('400 Level', "400 Level")
        
    ])
    department=models.CharField(max_length=200, default="Software Engineering",choices=[
        ('Software Engineering', "Software Engineering"),
        ('Computer Science', "Computer Science"),
        ('Nursing', "Nursing"),
        
    ])
    snippet = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    file = models.FileField(upload_to='staff_writings/', null=True, blank=True)

    def __str__(self):
        return self.title

class Departments(models.Model):
    title=models
class LibraryUpload(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    level=models.CharField(max_length=200, default="100 Level",choices=[
        ('100 Level', "100 Level"),
        ('200 Level', "200 Level"),
        ('300 Level', "300 Level"),
         ('400 Level', "400 Level")
        
    ])
    department=models.CharField(max_length=200, default="Software Engineering",choices=[
        ('Software Engineering', "Software Engineering"),
        ('Computer Science', "Computer Science"),
        ('Nursing', "Nursing"),
        
    ])
    snippet = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    file = models.FileField(upload_to='staff_writings/', null=True, blank=True)

    def __str__(self):
        return self.title