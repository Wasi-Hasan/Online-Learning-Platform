from django import forms
from .models import Course

class CourseUploadForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name', 'description', 'video', 'pdf']
