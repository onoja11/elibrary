from django.contrib.auth.forms import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, SetPasswordForm
from django import forms
from .models import Profile

class Student_Registration_Form(UserCreationForm):
	email=forms.EmailField(label="Email Address",
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': ' border  focus:ring-green-500 text-black text-sm rounded-lg block w-full p-2.5',
            'placeholder': 'name@gmail.com',
            'required': True,
        })
    )
	first_name=forms.CharField(label="First Name",
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': ' border  focus:ring-green-500 text-black text-sm rounded-lg block w-full p-2.5',
            'placeholder': 'first name',
            'required': True,
        })
    )
	last_name=forms.CharField(label="Last Name",
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': ' border  focus:ring-green-500 text-black text-sm rounded-lg block w-full p-2.5',
            'placeholder': 'last name',
            'required': True,
        })
    )
	username=forms.CharField(label="University Identification Number ",
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': ' border  focus:ring-green-500 text-black text-sm rounded-lg block w-full p-2.5',
            'placeholder': 'vugsen239508 or staff_no',
            'required': True,
        })
    )
	
	password1 = forms.CharField(label="Password",
        widget=forms.PasswordInput(attrs={
            'class': ' border  focus:ring-green-500 text-black text-sm rounded-lg block w-full p-2.5',
			 'placeholder': 'password.. must contain special chars',
            'required': True, 'id': 'password1' }))
	password2 = forms.CharField(label="Confirm Password",
        widget=forms.PasswordInput(attrs={
            'class': ' border  focus:ring-green-500 text-black text-sm rounded-lg block w-full p-2.5',
			 'placeholder': 'Re-enter password',
            'required': True,  'id': 'password2'}))
	usable_password = None

	class Meta:
		model=User
		fields=('username', 'first_name', 'last_name', 'email')
	def __init__(self,*args, **kwargs):
		super(Student_Registration_Form, self).__init__(*args, **kwargs)
		self.fields['password1'].help_text = ''
		self.fields['password2'].help_text = ''

class Staff_Registration_Form(UserCreationForm):
	email=forms.EmailField(label="Email Address",
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'border  focus:ring-green-500 text-white text-sm rounded-lg block w-full p-2.5',
            'placeholder': 'name@gmail.com',
            'required': True,
        })
    )
	first_name=forms.CharField(label="First Name",
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'bg-gray-700 border text-white text-sm rounded-lg block w-full p-2.5',
            'placeholder': 'first name',
            'required': True,
        })
    )
	last_name=forms.CharField(label="Last Name",
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'bg-gray-700 border text-white text-sm rounded-lg block w-full p-2.5',
            'placeholder': 'last name',
            'required': True,
        })
    )
	username=forms.CharField(label="Staff ID Number",
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'bg-gray-700 border text-white text-sm rounded-lg block w-full p-2.5',
            'placeholder': 'matriculation number',
            'required': True,
        })
    )
	
	password1 = forms.CharField(label="Password",
        widget=forms.PasswordInput(attrs={
            'class': 'bg-gray-700 border text-white text-sm rounded-lg block w-full p-2.5',
			 'placeholder': 'password.. must contain special chars',
            'required': True, }))
	password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'bg-gray-700 border text-white text-sm rounded-lg block w-full p-2.5',
			 'placeholder': 'Re-enter password',
            'required': True, }))
	usable_password = None

	class Meta:
		model=User
		fields=('username', 'first_name', 'last_name', 'email')
	def __init__(self,*args, **kwargs):
		super(Staff_Registration_Form, self).__init__(*args, **kwargs)
		self.fields['password1'].help_text = ''
		self.fields['password2'].help_text = ''
		self.fields['username'].label_attrs = {'class': 'text-white'}


class ProfileForm(forms.ModelForm):
  
    phone_number = forms.CharField(
        label="Phone Number",
        max_length=11,
        required=False,
        widget=forms.TextInput(attrs={
            'class': ' border text-black focus:ring-green-500 text-sm rounded-lg block w-full p-2.5',
            'placeholder': 'phone number',
        })
    )

    class Meta:
        model = Profile()
        fields = [ 'phone_number']

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        self.fields['phone_number'].help_text = ''