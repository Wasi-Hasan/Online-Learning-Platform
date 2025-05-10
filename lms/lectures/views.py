# lectures/views.py
from django.shortcuts import render, redirect
from django.contrib.admin.views.decorators import staff_member_required
from .forms import LectureForm
from .models import Lecture

@staff_member_required
def upload_lecture(request):
    if request.method == "POST":
        form = LectureForm(request.POST)
        if form.is_valid():
            form.save()  # Save the lecture to the database
            return redirect('lecture_list')  # Redirect to the lecture list page
    else:
        form = LectureForm()
    
    return render(request, 'lectures/upload_lecture.html', {'form': form})

def lecture_list(request):
    lectures = Lecture.objects.all()  # Get all lectures from the database
    return render(request, 'lectures/lecture_list.html', {'lectures': lectures})
