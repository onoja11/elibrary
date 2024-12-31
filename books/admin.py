from django.contrib import admin
from .models import Book,Borrowed_Book
# Register your models here.
admin.site.register(Book)
admin.site.register(Borrowed_Book)
