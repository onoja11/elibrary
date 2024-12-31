from django import forms
from .models import StaffWriting,LibraryUpload

class StaffWritingForm(forms.ModelForm):
    title=forms.CharField(label="Title",  max_length=100,
        widget=forms.TextInput(attrs={
            'class':'mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-green-500 focus:ring focus:ring-green-200 focus:ring-opacity-50'
        }))
    snippet=forms.CharField(label="Snippet",  max_length=150,
        widget=forms.Textarea(attrs={
            'class':'mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-green-500 focus:ring focus:ring-green-200 focus:ring-opacity-50'
        }))
  
    level=forms.ChoiceField(label="Level", choices=[
        ('100 Level', "100 Level"),
        ('200 Level', "200 Level"),
        ('300 Level', "300 Level"),
         ('400 Level', "400 Level")
        
    ], widget=forms.Select(attrs={
            'class':'mt-1 block w-full rounded-md border-green-300 shadow-sm focus:border-green-500 focus:ring focus:ring-green-200 focus:ring-opacity-50'
        }))
    department=forms.ChoiceField(label="Department",choices=[
        ('Software Engineering', "Software Engineering"),
        ('Computer Science', "Computer Science"),
        ('Nursing', "Nursing"),
        
    ], widget=forms.Select(attrs={
            'class':'mt-1 block w-full rounded-md border-green-300 shadow-sm focus:border-green-500 focus:ring focus:ring-green-200 focus:ring-opacity-50'
        }))
    class Meta:
        model = StaffWriting
        fields = ['title', 'snippet','department' ,'file','level']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 10}),
        }
class LibraryUploadsForm(forms.ModelForm):
    title=forms.CharField(label="Title",  max_length=100,
        widget=forms.TextInput(attrs={
            'class':'mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-green-500 focus:ring focus:ring-green-200 focus:ring-opacity-50'
        }))
    snippet=forms.CharField(label="Snippet",  max_length=150,
        widget=forms.Textarea(attrs={
            'class':'mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-green-500 focus:ring focus:ring-green-200 focus:ring-opacity-50'
        }))
  
    level=forms.ChoiceField(label="Level", choices=[
        ('100 Level', "100 Level"),
        ('200 Level', "200 Level"),
        ('300 Level', "300 Level"),
         ('400 Level', "400 Level")
        
    ], widget=forms.Select(attrs={
            'class':'mt-1 block w-full rounded-md border-green-300 shadow-sm focus:border-green-500 focus:ring focus:ring-green-200 focus:ring-opacity-50'
        }))
    department=forms.ChoiceField(label="Programme",choices=[
        ('Software Engineering', "Software Engineering"),
        ('Computer Science', "Computer Science"),
        ('Nursing', "Nursing"),
        
    ], widget=forms.Select(attrs={
            'class':'mt-1 block w-full rounded-md border-green-300 shadow-sm focus:border-green-500 focus:ring focus:ring-green-200 focus:ring-opacity-50'
        }))
    class Meta:
        model = LibraryUpload
        fields = ['title', 'snippet','department' ,'file','level']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 10}),
        }