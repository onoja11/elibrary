from django.urls import path
from .views import index_page, student_login_page,student_registration_page, student_home_page, student_borrow_page,staff_login_page,staff_home_page ,search_api,student_dashboard_page, profile_update,logout_user,global_search,lecturer_home_page,lecturer_login_page,nav_home,nav_dashboard
urlpatterns = [
    path("", index_page, name="index_page"),
    path("student_login/",student_login_page,name="student_login_page" ),
     path("student_registration/",student_registration_page,name="student_registration_page" ),
     path("student_home/", student_home_page, name="student_home_page"),
     path("nav_home/", nav_home, name="nav_home"),
     path("nav_dashboard/", nav_dashboard, name="nav_dashboard"),
     path("student_dashboard/", student_dashboard_page, name="student_dashboard_page"),
     path("student_borrow/", student_borrow_page,name="student_borrow_page"),
     path("staff_login/",staff_login_page,name="staff_login_page" ),
      path("staff_home/", staff_home_page, name="staff_home_page"),
        path("lecturer_login/",lecturer_login_page,name="lecturer_login_page" ),
      path("lecturer_home/", lecturer_home_page, name="lecturer_home_page"),
       path('api/search/', search_api, name='search_api'),
       path('profile_update/',profile_update,name="profile_update" ),
       path('logout/', logout_user,name="logout"),
        path("global_search/", global_search, name="global_search"),
       
]
