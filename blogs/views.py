from django.shortcuts import render, HttpResponseRedirect
from django.contrib import messages
from .forms import SignupForm, LoginForm
from django.contrib.auth import authenticate,login,logout
from .models import Post

# Homepage
def home(request):
    posts = Post.objects.all()
    return render(request, 'blogs/home.html', {'posts':posts})

# About
def about(request):
    return render(request, 'blogs/about.html')

# Contact
def contact(request):
    return render(request, 'blogs/contact.html')

# Dashboard
def dashboard(request):
    return render(request, 'blogs/dashboard.html')

# Signup
def signup(request):
    if request.method == 'POST':
        fm = SignupForm(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request, 'Account created successfully!')
            # return HttpResponseRedirect('/login/')
    else:
        fm = SignupForm()
    return render(request, 'blogs/signup.html', {'form':fm})

# Login
def user_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            fm = LoginForm(request=request, data=request.POST)
            if fm.is_valid():
                uname = fm.cleaned_data['username']
                upass = fm.cleaned_data['password']
                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'Logged in successfully!')
                    return HttpResponseRedirect('/dashboard/')
        else:
            fm = LoginForm()
        return render(request, 'blogs/login.html', {'form':fm})
    else:
        return HttpResponseRedirect('/dashboard/')

# Logout
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')
