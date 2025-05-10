from django.urls import path
from .views import (
    blogs_view,
    logout_view,
    profile_view,
    signup_view,
    login_view,
    home_view,
    contact_us_view
)

urlpatterns = [
    path('', signup_view, name='signup'),  # Signup page
        path('signup/', signup_view, name='signup'),

    path('login/', login_view, name='login'),  # Login page
path('contact_us/', contact_us_view, name='contact_us'),
    path('home/', home_view, name='home'),  # Home page
    path('profile/', profile_view, name='profile'),  # Profile page
    path('logout/', logout_view, name='logout'),  # Logout functionality
    path('blogs/', blogs_view, name='blogs'),  # Blogs page
]
