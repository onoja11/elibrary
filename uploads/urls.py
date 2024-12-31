from django.urls import path
from .views import staff_writing_upload_page,file_download,student_material_view,get_departments_and_levels,library_upload_page,lib_material_view
urlpatterns = [
      path('', staff_writing_upload_page, name='staff_writing_upload_page'),
      path('library_upload/',library_upload_page, name='library_upload_page'),
         path('download/<int:writing_id>/',file_download, name='file_download'),
         path('material_view/', student_material_view, name='student_material_view_page'),
           path('lib_material_view/', lib_material_view, name='lib_material_view_page'),
         path('get_dept', get_departments_and_levels, name="get_departments_and_levels")
]
