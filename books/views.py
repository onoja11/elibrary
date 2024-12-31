from django.shortcuts import render,redirect,get_object_or_404
from .forms import Book_Form,Borrow_Form
from .models import Book,Borrowed_Book
from django.contrib import messages
from core.models import Profile
from django.db.models import Q
from django.http import JsonResponse
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.urls import reverse
from django.utils import timezone
from django.template.loader import render_to_string

# Create your views here.
def staff_add_page(request):
    if request.user.is_authenticated:
        profile = Profile.objects.get(user__id=request.user.id)
        if profile.status!="libstaff":
            return redirect("student_login_page")
        form=Book_Form()
        if request.POST:
            form=Book_Form(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, "Book Added Successfully")
                return redirect("staff_inventory_page")
            else:
                messages.success(request, form.errors)
                return redirect("staff_add_page")
        else:
            return render(request, "books/staff_add.html", {"form": form})
    else:
        messages.success(request, "Please login first")
        return redirect("student_login_page")
            
def staff_inventory_page(request):
    if request.user.is_authenticated:
        profile = Profile.objects.get(user__id=request.user.id)
        if profile.status!="libstaff":
            return redirect("student_login_page")
        books=Book.objects.all()
        p=Paginator(books,10)
        page_number=request.GET.get('page')
        try:
            books=p.get_page(page_number)
        except PageNotAnInteger:
            books=p.page(1)
        except EmptyPage:
            books=p.page(p.num_pages)
        return render(request, "books/staff_inventory.html", {"books":books})
    else:
        messages.success(request, "Please login first")
        return redirect("staff_login_page")
    


    
from django.http import JsonResponse
from django.db.models import Q

def staff_borrowview_page(request):
    if request.user.is_authenticated:
        search_query = request.GET.get('search', '')
        books = Borrowed_Book.objects.all()

        if search_query:
            books = books.filter(
                Q(Book__Title__icontains=search_query) |
                Q(User__username__icontains=search_query)
            )

        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            # This is an AJAX request, return JSON data
            books_data = [{
                'id': book.id,
                'title': book.Book.Title,
                'borrower': book.User.username,
                'borrowed_date': book.Borrowed_Date.strftime('%Y-%m-%d'),
                'return_date': book.Return_Date.strftime('%Y-%m-%d'),
                'overdue': book.Overdue,
                'returned': book.Returned,
            } for book in books]
            return JsonResponse({'books': books_data})
        else:
            # This is a regular request, render the full page
            return render(request, "books/staff_borrowview.html", {"books": books})
    else:
        messages.success(request, "Please login first")
        return redirect("staff_login_page")
    
def staff_borrowaction_page(request, id):
    if request.user.is_authenticated:
        profile = Profile.objects.get(user__id=request.user.id)
        if profile.status!="libstaff":
            return redirect("student_login_page")
        print( Borrowed_Book.objects.get(id=id))
        return render(request, "books/staff_borrowaction.html",{"book": Borrowed_Book.objects.get(id=id)})
    else:
        messages.success(request, "Please login first")
        return redirect("staff_login_page")

def book_view_page(request, id):
    if request.user.is_authenticated:
        return render(request, "books/book_view.html",{"book": Book.objects.get(id=id)})
    else:
        messages.success(request, "Please login first")
        return redirect("student_login_page")

def book_return(request,id):
    if request.user.is_authenticated:
        profile = Profile.objects.get(user__id=request.user.id)
        if profile.status!="libstaff":
            return redirect("student_login_page")
        book=Borrowed_Book.objects.get(id=id)
        book.Returned=True
        book.save()
        return redirect("staff_borrowview_page")
    else:
        messages.success(request, "Please login first")
        return redirect("staff_login_page")
from datetime import datetime

def book_borrow_page(request, book_id):
    if request.user.is_authenticated:
        strike=0
        form = Borrow_Form()
        if request.POST:
            form = Borrow_Form(request.POST)
            if form.is_valid():
                book = get_object_or_404(Book, id=book_id)
                
                print( book)
                # Check if the book has already been borrowed by the same user
                if Borrowed_Book.objects.filter(Book=book, User=request.user).exists():
                    messages.error(request, "You have already borrowed this book.")
                    return redirect("nav_home")
                else:
                    
                    for book in Borrowed_Book.objects.filter(User=request.user):
                        #print(book)
                        if book.Overdue==True and book.Returned==False:
                            print("jiggerboo")
                            strike+=1
                            if strike>=1:
                            
                                messages.error(request, "Please return all overdue books ,before borrowing.")
                                return redirect("overdue")
                        print(strike)
                    borrowed_book = form.save(commit=False)
                    print("Aa")
                    print(borrowed_book)
                    #borrowed_book.Book = book
                    borrowed_book.User = request.user
                    #borrowed_book.Borrow_Date = datetime.now()
                    if borrowed_book.Return_Date < borrowed_book.Borrowed_Date:
                        messages.error(request, "Return date cannot be earlier than borrow date.")
                        return redirect("books/book_borrow.html")
                    borrowed_book.save()
                    messages.success(request, "Book borrowed successfully.")
                    return redirect("nav_home")
            else:
                return redirect("student_borrow_page")
        
        return render(request, "books/book_borrow.html", {"book": Book.objects.get(id=book_id), "form": form})
    else:
        messages.success(request, "Please login first")
        return redirect("student_login_page")
def borrow_search_page(request):
    search_query = request.GET.get('search', '')

    books = Borrowed_Book.objects.all()
    if search_query:
        books = Borrowed_Book.objects.filter(
        Q(Book__Title__icontains=search_query) | 
        Q(User__username__icontains=search_query)
    )
    
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        books_data = [
            {
                'id': book.pk,
                'Book': {'Title': book.Book.Title},
                'User': {'username': book.User.username},
                'Borrowed_Date': book.Borrowed_Date,
                'Return_Date': book.Return_Date,
                'Overdue': book.Overdue,
                'Returned': book.Returned
            } for book in books
        ]
        return JsonResponse(books_data, safe=False)
    
    return render(request, 'books/staff_borrowview.html', {'books': books})

def barcode_scan_page(request):
    return render(request, 'books/barcode_scan.html')

def process_barcode(request):
    barcode = request.GET.get('barcode')
    try:
        book = get_object_or_404(Book, isbn=barcode)
        return JsonResponse({
            'success': True,
            'redirect_url': reverse('book_detail', args=[book.id])
        })
    except Book.DoesNotExist:
        return JsonResponse({
            'success': False,
            'error': 'Book not found'
        })

def overdue_fine(request):
    if request.user.is_authenticated:
        return render(request, "books/overdue_fine.html")
    else:
        messages.success(request, "Please login first")
        return redirect("student_login_page")

'''
import stripe
from django.conf import settings
from django.shortcuts import redirect
from django.views import View


stripe.api_key = settings.STRIPE_SECRET_KEY

class CreateStripeCheckoutSessionView(View):
    """
    Create a checkout session and redirect the user to Stripe's checkout page
    """

    def post(self, request, *args, **kwargs):
        #price = Price.objects.get(id=self.kwargs["pk"])

        checkout_session = stripe.checkout.Session.create(
            payment_method_types=["card"],
            line_items=[
                {
                    "price_data": {
                        "currency": "usd",
                        "unit_amount": int(1000) ,
                        "product_data": {
                            "name": "Overdue fine",
                            "description":"Too late bro",
                          
                        },
                    }
                }
            ],
           
            mode="payment",
            success_url=settings.PAYMENT_SUCCESS_URL,
            cancel_url=settings.PAYMENT_CANCEL_URL,
        )
        return redirect(checkout_session.url)
'''

# views.py
import stripe
from django.conf import settings
from django.shortcuts import render, redirect
from django.http import JsonResponse
#from .models import Fine  # Assuming you have a Fine model
from django.views.decorators.csrf import csrf_exempt

stripe.api_key = settings.STRIPE_SECRET_KEY

def overdue_fine(request):
    return render(request, 'books/overdue_fine.html', {
        'stripe_publishable_key': settings.STRIPE_PUBLISHABLE_KEY
    })

@csrf_exempt
def process_payment(request):
    if request.method == 'POST':
        try:
            amount = int(request.POST['amount']) * 100  # Amount in cents
            token = request.POST['stripeToken']
            
            # Create Stripe charge
            charge = stripe.Charge.create(
                amount=amount,
                currency='usd',
                description='Overdue fine payment',
                source=token,
            )
            
            # Update fine status in the database here
            # For example: Fine.objects.filter(id=some_id).update(paid=True)

            return JsonResponse({'status': 'Payment successful'})
        except Exception as e:
            return JsonResponse({'status': 'Payment failed', 'error': str(e)})
    return JsonResponse({'status': 'Invalid request'}, status=400)

