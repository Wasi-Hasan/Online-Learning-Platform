# lectures/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.upload_lecture, name='upload_lecture'),
    path('list/', views.lecture_list, name='lecture_list'),  # Use this name in templates or views
]
