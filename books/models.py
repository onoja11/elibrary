from django.db import models
from django.contrib.auth.models import User
import datetime
# Create your models here.
class Book(models.Model):
    Title=models.CharField(max_length=100)
    Author=models.CharField(max_length=100)
    Category=models.CharField(max_length=100, choices=[
    ("A", "General Works"),
    ("B", "Philosophy, Psychology, Religion"),
    ("C", "Auxiliary Sciences of History"),
    ("D", "World History and History of Europe, Asia, Africa, Australia, New Zealand, etc."),
    ("E", "History of America"),
    ("F", "History of the Americas"),
    ("G", "Geography, Anthropology, and Recreation"),
    ("H", "Social Sciences"),
    ("J", "Political Science"),
    ("K", "Law"),
    ("K", "Journals and reference books"),
    ("KA", "Jurisprudence"),
    ("KB", "General and comparative law"),
    ("KC", "International law"),
    ("KD", "Religious legal systems"),
    ("KE", "Ancient and medieval law"),
    ("KF-KN", "Common law"),
    ("KF", "British Isles"),
    ("KG", "Canada, US, West Indies"),
    ("KH", "Australia, New Zealand"),
    ("KL", "General"),
    ("KM", "Public law"),
    ("KN", "Private law"),
    ("KP", "Preferred jurisdiction"),
    ("KR", "Africa"),
    ("KS", "Latin America"),
    ("KT", "Asia and Pacific"),
    ("KV", "Europe"),
    ("KW", "European Community Law (alternative)"),
    ("KZ", "Non-legal subjects"),
    ("L", "Education"),
    ("M", "Music"),
    ("N", "Fine Arts"),
    ("P", "Language and Literature"),
    ("Q", "Science"),
    ("R", "Medicine"),
    ("S", "Agriculture"),
    ("T", "Technology"),
    ("U", "Military Science"),
    ("V", "Naval Science"),
    ("Z", "Bibliography, Library Science, and General Information Resources")
], default="Science")
    Year_Released=models.IntegerField()
    Edition=models.CharField(max_length=10)
    Shelf_Number=models.CharField(max_length=20)
    ISBN_Number=models.CharField(max_length=13, default="0000000000000",null=True)
    Number_of_Copies=models.DecimalField(max_digits=100,decimal_places=1)
    def __str__(self):
        return self.Title

class Borrowed_Book(models.Model):
    Book=models.ForeignKey(Book,on_delete=models.CASCADE, default=1)
    User = models.ForeignKey(User, on_delete=models.CASCADE, null=True,blank=True)
    Borrowed_Date=models.DateField(default=datetime.datetime.today)
    Return_Date=models.DateField(default=datetime.datetime.today)
    Returned=models.BooleanField(default=False)
    Overdue=models.BooleanField(default=False)
    
    def __str__(self):
        return self.Book.Title

'''
python manage.py makemigrations
python manage.py migrate
python manage.py runserver




'''