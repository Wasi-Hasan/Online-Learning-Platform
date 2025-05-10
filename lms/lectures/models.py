# lectures/models.py
from django.db import models

class Lecture(models.Model):
    name = models.CharField(max_length=255) 
    exercises = models.TextField() 
    sample_codes = models.TextField()  
    project_ideas = models.TextField()  
    frameworks = models.CharField(max_length=255)  

    def __str__(self):
        return self.name
