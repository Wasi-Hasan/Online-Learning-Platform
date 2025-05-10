import debug_toolbar
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('users.urls')),  # Include URLs from the users app
    path('courses/', include('courses.urls')),  # Include URLs from the courses app
        path('lectures/', include('lectures.urls')),  # Add this line to include lecture URLs


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
