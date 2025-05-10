from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.core.mail import send_mail
from django.conf import settings


from .forms import SignupForm, LoginForm

def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            print(f"User {user.username} logged in successfully!")  # Debugging line
            return redirect('home')
        else:
            print("Form is invalid!")  # Debugging line
    form = LoginForm()
    return render(request, 'login.html', {'form': form})


@login_required
def home_view(request):
    return render(request, 'home.html')
@login_required
def blogs_view(request):
    return render(request, 'blogs.html')

@login_required  # Ensures the user is logged in
def profile_view(request):
    # Pass the user details to the template
    return render(request, 'profile.html', {
        'username': request.user.username,
        'email': request.user.email,
        'password': request.user.password  # Note: Don't display the actual password
    })
def logout_view(request):
    logout(request)  # Logs the user out
    return redirect('signup')  # Redirects to the signup page (change 'signup' if needed)
def contact_us_view(request):
    message = None
    message_class = None

    if request.method == 'POST':
        subject = request.POST['subject']
        message_body = request.POST['message']
        user_email = request.user.email if request.user.is_authenticated else 'Anonymous User'
        
        # Compose the email
        email_message = f"Feedback from {user_email}:\n\n{message_body}"
        
        try:
            send_mail(
                subject=subject,
                message=email_message,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=['ayan3092003@gmail.com'],
            )
            message = "Your feedback has been sent successfully!"
            message_class = "success"
        except Exception as e:
            print(e)
            message = "There was an error sending your feedback. Please try again."
            message_class = "error"

    return render(request, 'contact_us.html', {'message': message, 'message_class': message_class})
