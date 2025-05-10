from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    video = models.FileField(upload_to='courses/videos/', null=True, blank=True)
    pdf = models.FileField(upload_to='courses/pdfs/', null=True, blank=True)

    def __str__(self):
        return self.name
