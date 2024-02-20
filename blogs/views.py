from django.shortcuts import render, HttpResponseRedirect

# Homepage
def home(request):
    return render(request, 'blogs/home.html')

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
    return render(request, 'blogs/signup.html')

# Login
def login(request):
    return render(request, 'blogs/login.html')

# Logout
def user_logout(request):
    return HttpResponseRedirect('/')
