from django.shortcuts import render, redirect
from .models import Course
from .forms import CourseUploadForm
from django.contrib.auth.decorators import login_required
from django.core.cache import cache


def courses(request):
    courses = Course.objects.all()
    return render(request, 'courses/courses.html', {'courses': courses})

@login_required
def upload_course(request):
    if request.method == 'POST':
        form = CourseUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('courses')
    else:
        form = CourseUploadForm()
    return render(request, 'courses/upload_course.html', {'form': form})
