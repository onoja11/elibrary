from django.contrib.auth.forms import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, SetPasswordForm
from django import forms
from .models import Book,Borrowed_Book

class Book_Form(forms.ModelForm):
    Title = forms.CharField(
        label='Title',
        max_length=200,
        required=True,
        widget=forms.TextInput(attrs={'id': 'title'})
    )
    Author = forms.CharField(
        label='Author',
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={'id': 'author'})
    )
    Category = forms.ChoiceField(
        label='Category',
        required=True,
   
choices = [
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
]
,
        widget=forms.Select(attrs={'id': 'author'})
    )
    Year_Released = forms.IntegerField(
        label='Year Released',
        required=True,
        widget=forms.NumberInput(attrs={'id': 'year'})
    )
    Edition = forms.CharField(
        label='Edition',
        max_length=50,
        required=False,
        widget=forms.TextInput(attrs={'id': 'edition'})
    )
    Shelf_Number = forms.CharField(
        label='Shelf Number',
        max_length=50,
        required=True,
        widget=forms.TextInput(attrs={'id': 'shelf'})
    )
    ISBN_Number = forms.CharField(
        label='ISBN_Number',
        max_length=50,
        required=True,
        widget=forms.TextInput(attrs={'id': 'shelf'})
    )
    Number_of_Copies = forms.IntegerField(
        label='Number of Copies',
        required=True,
        widget=forms.NumberInput(attrs={'id': 'copies'})
    )

    class Meta:
        labels = {
            'Title': 'Title',
            'Author': 'Author',
            'Year_Released': 'Year Released',
            'Edition': 'Edition',
            'Shelf_Number': 'Shelf Number',
            'Number_of_Copies': 'Number of Copies',
            'ISBN_Number':'ISBN_Number'
        }
        model=Book
        fields=("Title", "Author","Year_Released", "Edition","ISBN_Number", "Shelf_Number",'Category', "Number_of_Copies")

class Borrow_Form(forms.ModelForm):
    Borrowed_Date = forms.DateField(
        label='Date Borrowed',
        required=True,
         widget=forms.DateInput(format="%Y-%m-%d", attrs={"type": "date",'placeholder': 'd',
            'required': True,}),
        input_formats=["%Y-%m-%d"]
    
    )
    Return_Date = forms.DateField(
        label='Date of Return',
        required=True,
        widget=forms.DateInput(format="%Y-%m-%d", attrs={"type": "date"}),
        input_formats=["%Y-%m-%d"]
    
    )
    class Meta:
    
        model=Borrowed_Book
        fields=("Borrowed_Date", "Return_Date")
        
'''
class StaffWritingForm(forms.ModelForm):
    class Meta:
        model = StaffWriting
        fields = ['title', 'content', 'file']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 10}),
        }'''