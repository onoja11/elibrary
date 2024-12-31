from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.models import User
from books.models import Borrowed_Book
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils import timezone

from books.models import Book, Borrowed_Book
from django.http import JsonResponse
from django.db.models import Q
from .models import Profile
from .forms import Student_Registration_Form,Staff_Registration_Form, ProfileForm
# Create your views here.
def index_page(request):
    return render(request, ("core/index.html"))


def student_login_page(request):
    if request.POST:
        username=request.POST["username"]
        password=request.POST["password"]
        
        user=authenticate(request, username=username, password=password)
        if user is not None: 
            login(request, user)
            messages.success(request, ("You have been logged in"))
            return redirect("student_home_page")
        else:
            messages.success(request, ("Invalid credentials supplied"))

           # return redirect("student_login_page")
    

    return render(request, "core/student_login.html")

def student_registration_page(request):
    form =Student_Registration_Form()
    if request.method=="POST":
        form=Student_Registration_Form(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data["username"]
            word1=form.cleaned_data["password1"]
            word2=form.cleaned_data["password2"]
            if word1!=word2:
                messages.success(request, (form.errors))
                return redirect("student_registration_page")
            password=form.cleaned_data["password1"]
            user=authenticate(username=username, password=password)
            login(request, user)
            return redirect("profile_update")
        else:
            messages.success(request, (form.errors))
          #  return redirect("student_registration_page")

    return render(request, "core/student_registration.html", {"form":form})

def student_home_page(request):
    if request.user.is_authenticated:

        return render (request, "core/student_home.html")
    else:
        messages.success(request, "Please login first")
        return redirect("student_login_page")

def nav_home(request):
    if request.user.is_authenticated:
        profile = Profile.objects.get(user__id=request.user.id)
        if profile.status=="libstaff":
            return redirect("staff_home_page")
        elif profile.status=="lecturer":
            return redirect("lecturer_home_page")
        return redirect("student_home_page")
    else:
        messages.success(request, "Please login first")
        return redirect("student_login_page")
def nav_dashboard(request):
    if request.user.is_authenticated:
        profile = Profile.objects.get(user__id=request.user.id)
        if profile.status=="libstaff":
            return redirect("staff_home_page")
        elif profile.status=="lecturer":
            return redirect("lecturer_home_page")
        return redirect("student_dashboard_page")
    else:
        messages.success(request, "Please login first")
        return redirect("student_login_page")
def student_borrow_page(request):
    return render (request, "core/student_borrow.html")
def student_dashboard_page(request):
    current_date = timezone.now().date()
    
    # Get all borrowed books for the current user
    books = Borrowed_Book.objects.filter(User__id=request.user.id)
    #print(books)
    # Check for overdue books and update their status
    for book in books:
        
        if book.Return_Date < current_date:
            print("fff")
            book.Overdue = True
            
            book.save()
            # if book.Overdue:
            #     return redirect('overdue')
        else:
            book.Overdue = False
            book.save()
    books=Borrowed_Book.objects.filter(User__id=request.user.id)
    profile = Profile.objects.get(user__id=request.user.id)
    print(books)
    print("hey")
    return render(request, "core/student_dashboard.html", {"books":books, "profile":profile})
def staff_login_page(request):
    if request.POST:
        username=request.POST["username"]
        password=request.POST["password"]
        if not username.startswith("lib"):
            messages.error(request, "Staff usernames not valid")
            return redirect("staff_login_page")
        user=authenticate(request, username=username, password=password)
        if user is not None:
           

            login(request, user)
           
            messages.success(request, ("You have been logged in"))
            return redirect("staff_home_page")
        else:
            messages.success(request, ("Inavlid credentials supplied"))
            return redirect("staff_login_page")

    return render(request, "core/staff_login.html")


def lecturer_login_page(request):
    if request.POST:
        username=request.POST["username"]
        password=request.POST["password"]
        if not username.startswith("lecturer"):
            messages.error(request, "Detail provided not valid")
            
            return redirect("lecturer_login_page")
        user=authenticate(request, username=username, password=password)
        if user is not None:
           

            login(request, user)
           
            messages.success(request, ("You have been logged in"))
            return redirect("lecturer_home_page")
        else:
            messages.success(request, ("Inavlid credentials supplied"))
            

    return render(request, "core/lecturer_login.html")


def staff_home_page(request):
    current_date = timezone.now().date()
    
    # Get all borrowed books for the current user
    books = Borrowed_Book.objects.all()
    # Check for overdue books and update their status
    for book in books:
        
        if book.Return_Date < current_date:
            print("fff")
            book.Overdue = True
            book.save()
        else:
            book.Overdue = False
            book.save()
    book_count=Book.objects.count()
    borrowed_book_count=Borrowed_Book.objects.count()
    user_count=User.objects.count()
    overdue_count=Borrowed_Book.objects.filter(Overdue=True).count()
    if request.user.is_authenticated:
        profile = Profile.objects.get(user__id=request.user.id)
        if profile.status!="libstaff":
            return redirect("student_login_page")
        return render (request, "core/staff_home.html",{"profile": profile, "book_count":book_count, "borrowed_book_count":borrowed_book_count, "user_count":user_count, "overdue_count":overdue_count}, )
    else:
        messages.success(request, "Please login first")
        return redirect("staff_login_page")

def lecturer_home_page(request):
    books = Borrowed_Book.objects.filter(User__id=request.user.id)
    current_date = timezone.now().date()
    
    # Get all borrowed books for the current user
    books = Borrowed_Book.objects.all()
    # Check for overdue books and update their status
    for book in books:
        
        if book.Return_Date < current_date:
            book.Overdue = True
            book.save()
        else:
            book.Overdue = False
            book.save()
  
    if request.user.is_authenticated:
        profile = Profile.objects.get(user__id=request.user.id)
        if profile.status!="lecturer":
            return redirect("student_login_page")
        return render (request, "core/lecturer_home.html",{"profile": profile, "books":books}, )
    else:
        messages.success(request, "Please login first")
        return redirect("lecturer_login_page")


def search_api(request):
    query = request.GET.get('q', '')
    if query:
    #    products = Product.objects.filter(Q(name__icontains=searched) | Q(description__icontains=searched))

        results = Book.objects.filter(Q(Author__icontains=query) | Q(Title__icontains=query)|Q(Shelf_Number__icontains=query)|Q(Year_Released__icontains=query)).values("id","Title", "Author","Year_Released", "Edition", "Shelf_Number", "Number_of_Copies")
        return JsonResponse(list(results), safe=False)
    return JsonResponse([], safe=False)

@login_required
def profile_update(request):
    if request.user.is_authenticated:

        current_user_profile = Profile.objects.get(user__id=request.user.id)
        form = ProfileForm(request.POST or None, instance=current_user_profile)
        
        if request.method == 'POST':
            if form.is_valid():
                form.save()
                messages.success(request, "Profile updated successfully!")
                return redirect("student_dashboard_page")
            else:
                messages.error(request, form.errors)
        
        return render(request, "core/profile_update.html", {"form": form}) 
    else:
        messages.success(request, "Please signup first")
        return redirect("student_registration_page")

def logout_user(request):
    messages.success(request, ("You have been logged out.. Thanks"))
    logout(request)
    return redirect("index_page")

def custom_404(request,exception):
    return render(request, "core/404.html")


def global_search(request):
    if request.user.is_authenticated:

        return render (request, "core/global_search.html")
    else:
        messages.success(request, "Please login first")
        return redirect("staff_login_page")

