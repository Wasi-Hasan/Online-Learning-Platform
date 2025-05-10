from django.urls import path
from . import views

urlpatterns = [
    path('', views.courses, name='courses'),
    path('upload/', views.upload_course, name='upload_course'),
]
