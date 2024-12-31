from django.urls import path
from .views import staff_add_page,staff_inventory_page, book_view_page,book_borrow_page,staff_borrowview_page,staff_borrowaction_page,book_return,borrow_search_page,barcode_scan_page,process_barcode,overdue_fine,process_payment

#,staff_writing_upload
urlpatterns = [
    path("staff_add/", staff_add_page, name="staff_add_page" ),
     path("staff_inventory/", staff_inventory_page, name="staff_inventory_page" ),
     path("book_view/<int:id>", book_view_page, name="book_view_page"),
      path("book_borrow/<int:book_id>", book_borrow_page, name="book_borrow_page"),
      path("staff_borrowview/", staff_borrowview_page, name="staff_borrowview_page"),
      path("staff_borrowaction/<int:id>", staff_borrowaction_page,name="staff_borrowaction_page"),
      path("return_book/<int:id>/",book_return,name="return_book"),
      path("borrow_search/", borrow_search_page, name="borrow_search_page"),
        path('barcode_scan/', barcode_scan_page, name='barcode_scan_page'),
    path('process-barcode/', process_barcode, name='process_barcode'),
    path('overdue/', overdue_fine, name='overdue'),
   
    path('process/', process_payment,name="process_payment")
  
]
