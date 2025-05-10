# lectures/forms.py
from django import forms
from .models import Lecture

class LectureForm(forms.ModelForm):
    class Meta:
        model = Lecture
        fields = ['name', 'exercises', 'sample_codes', 'project_ideas', 'frameworks']
