from django.shortcuts import render, HttpResponseRedirect
from django.contrib import messages
from .forms import SignupForm, LoginForm, PostForm, EditAdminProfileForm, EditUserProfileForm, ChangeUserPassword
from django.contrib.auth import authenticate,login,logout, update_session_auth_hash
from .models import Post
from django.contrib.auth.models import Group

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
    if request.user.is_authenticated:
        posts = Post.objects.all()
        user = request.user
        gps = user.groups.all()
        return render(request, 'blogs/dashboard.html', {'posts':posts, 'user':user, 'groups':gps})
    else:
        return HttpResponseRedirect('/login/')

# Signup
def signup(request):
    if request.method == 'POST':
        fm = SignupForm(request.POST)
        if fm.is_valid():
            messages.success(request, 'Account created successfully!')
            user = fm.save()
            group = Group.objects.get(name='Author')
            user.groups.add(group)
            return HttpResponseRedirect('/login/')
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


# Add post  
def add_post(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            fm = PostForm(request.POST)
            if fm.is_valid():
                fm.save()
                messages.success(request,'New Post Added Successfully!')
                fm = PostForm()
        else:
            fm = PostForm()
        return render(request, 'blogs/addpost.html',{'form':fm})
    else:
        return HttpResponseRedirect('/login/')

# Update Post   
def update_post(request, id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            pi = Post.objects.get(pk=id)
            fm = PostForm(request.POST, instance=pi)
            if fm.is_valid():
                fm.save()
                messages.success(request, 'Post Updated Successfully')
        else:
            pi = Post.objects.get(pk=id)
            fm = PostForm(instance=pi)
        return render(request, 'blogs/updatepost.html', {'form':fm})
    else:
        return HttpResponseRedirect('/login/')
    
# Delete Post
def delete_post(request, id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            pi = Post.objects.get(pk=id)
            pi.delete()
            return HttpResponseRedirect('/dashboard')
    else:
        return HttpResponseRedirect('/login/')
    
# User Profile
def user_profile(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            if request.user.is_superuser == True:
                fm = EditAdminProfileForm(request.POST, instance=request.user)
                # users = User.objects.all()
            else:
                fm = EditUserProfileForm(request.POST, instance=request.user)
            if fm.is_valid():
                fm.save()
                messages.success(request, 'Profile updated successfully!')
        else:
            if request.user.is_superuser == True:
                fm = EditAdminProfileForm(instance=request.user)
            else:
                fm = EditUserProfileForm(instance=request.user)
        return render(request, 'blogs/profile.html', {'form':fm})
    else:
        return HttpResponseRedirect('/login/')
    
# Change user password
def change_pass(request):
    if request.method == 'POST':
        fm = ChangeUserPassword(user=request.user, data=request.POST)
        if fm.is_valid():
            fm.save()
            update_session_auth_hash(request, fm.user)
            messages.success(request, 'Password changed successfully!')
    else:
        fm = ChangeUserPassword(user=request.user)
    return render(request, 'blogs/changepass.html', {'form':fm})