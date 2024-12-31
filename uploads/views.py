from django.shortcuts import render,redirect,get_object_or_404, HttpResponse
from .models import StaffWriting,LibraryUpload
from .forms import StaffWritingForm,LibraryUploadsForm
from django.contrib import messages
from django.http import FileResponse
from django.db.models import Q
from django.http import JsonResponse
from django.template.loader import render_to_string
def staff_writing_upload_page(request):
    writings = StaffWriting.objects.all().order_by('-created_at')
    
    if request.method == 'POST':
        form = StaffWritingForm(request.POST, request.FILES)
        if form.is_valid():
            writing = form.save(commit=False)
            writing.author = request.user
            writing.save()
            messages.success(request, 'Your writing has been uploaded successfully!')
            return redirect('staff_writing_upload_page')
    else:
        form = StaffWritingForm()
    

    return render(request, 'uploads/staff_writing_upload.html', {
        'form': form,
        'writings': writings,
    })
    
    
def library_upload_page(request):
    writings = LibraryUpload.objects.all().order_by('-created_at')
    
    if request.method == 'POST':
        form = LibraryUploadsForm(request.POST, request.FILES)
        if form.is_valid():
            writing = form.save(commit=False)
            writing.author = request.user
            writing.save()
            print(writings)
            messages.success(request, 'Your writing has been uploaded successfully!')
            return redirect('library_upload_page')
    else:
        form = LibraryUploadsForm()
    

    return render(request, 'uploads/lib_upload.html', {
        'form': form,
        'writings': writings,
    })
    
        
def staff_writing_detail(request, writing_id):
    writing = get_object_or_404(StaffWriting, id=writing_id)
    return render(request, 'staff_writing_detail.html',  {
        'writing': writing
    })    

def file_download(request, writing_id):
    file = get_object_or_404(StaffWriting, pk=writing_id)
    file_path = file.file.path
    response = FileResponse(open(file_path, 'rb'))
    response['Content-Type'] = 'application/pdf'
    response['Content-Disposition'] = f'attachment; filename="{file.title}.pdf"'
    return response
'''
def student_material_view(request):
    writings = StaffWriting.objects.all().order_by('-created_at')
    return render(request, 'uploads/student_material_download.html',{    'writings': writings,})
'''

def student_material_view(request):
    writings = StaffWriting.objects.all().order_by('-created_at')
    #department_filter = request.GET.get('department')
    search_query = request.GET.get('search','')
    
    #if department_filter and department_filter != 'All':
     #   documents = documents.filter(department__name=department_filter)
    
    if search_query:
        writings = writings.filter(Q(title__icontains=search_query))
        writings = StaffWriting.objects.all()
    search_query = request.GET.get('search', '')
    department = request.GET.get('department', '')
    level = request.GET.get('level', '')


    if department:
        writings = writings.filter(department=department)
    if level:
        writings = writings.filter(level=level)


    context = {
        'writings': writings,
    #    'departments': departments,
    #    'selected_department': department_filter,
        'search_query': search_query,
    }
    
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        html = render_to_string('uploads/partials/document_list.html', context)
        return JsonResponse({'html': html})
    return render(request, 'uploads/student_material_download.html',{    'writings': writings,})

def lib_material_view(request):
    writings = LibraryUpload.objects.all().order_by('-created_at')
    #department_filter = request.GET.get('department')
    search_query = request.GET.get('search','')
    
    #if department_filter and department_filter != 'All':
     #   documents = documents.filter(department__name=department_filter)
    
    if search_query:
        writings = writings.filter(Q(title__icontains=search_query))
        writings = LibraryUpload.objects.all()
    search_query = request.GET.get('search', '')
    department = request.GET.get('department', '')
    level = request.GET.get('level', '')


    if department:
        writings = writings.filter(department=department)
    if level:
        writings = writings.filter(level=level)


    context = {
        'writings': writings,
    #    'departments': departments,
    #    'selected_department': department_filter,
        'search_query': search_query,
    }
    
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        html = render_to_string('uploads/partials/document_list.html', context)
        return JsonResponse({'html': html})
    return render(request, 'uploads/lib_upload_download.html',{    'writings': writings,})

def get_departments_and_levels(request):
    departments = StaffWriting.objects.values_list('department', flat=True).distinct()
    levels = StaffWriting.objects.values_list('level', flat=True).distinct()
    return JsonResponse({
        'departments': list(departments),
        'levels': list(levels)
    })