from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from django.forms import widgets
from .models import Post

class SignupForm(UserCreationForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='Confirm Password (again)', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']
        widgets = {'username': forms.TextInput(attrs={'class':'form-control'}),
                   'first_name': forms.TextInput(attrs={'class':'form-control'}),
                   'last_name': forms.TextInput(attrs={'class':'form-control'}),
                   'email': forms.EmailInput(attrs={'class':'form-control'}),
                   }

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        labels = {'desc':'Description',}
        widgets = {'title':forms.TextInput(attrs={'class':'form-control'}),
                   'desc':forms.Textarea(attrs={'class':'form-control'}),
                   }
        
class EditUserProfileForm(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','date_joined']
        widgets = {'username': forms.TextInput(attrs={'class':'form-control'}),
                   'first_name': forms.TextInput(attrs={'class':'form-control'}),
                   'last_name': forms.TextInput(attrs={'class':'form-control'}),
                   'email': forms.EmailInput(attrs={'class':'form-control'}),
                   'date_joined': forms.DateTimeInput(attrs={'class':'form-control'}),
                   }

class EditAdminProfileForm(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = '__all__'
        widgets = {'password': forms.TextInput(attrs={'class':'form-control'}),
                   'last_login': forms.TextInput(attrs={'class':'form-control'}),
                   'is_superuser': forms.CheckboxInput(),
                   'groups': forms.Select(attrs={'class':'form-control'}),
                   'user_permissions': forms.SelectMultiple(attrs={'class':'form-control'}),
                   'username': forms.TextInput(attrs={'class':'form-control'}),
                   'first_name': forms.TextInput(attrs={'class':'form-control'}),
                   'last_name': forms.TextInput(attrs={'class':'form-control'}),
                   'email': forms.EmailInput(attrs={'class':'form-control'}),
                   'is_staff': forms.CheckboxInput(),
                   'is_active': forms.CheckboxInput(),
                   'date_joined': forms.DateTimeInput(attrs={'class':'form-control'}),
                   
                   }

class ChangeUserPassword(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    new_password1 = forms.CharField(label='New Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    new_password2 = forms.CharField(label='Confirm Password (again)',widget=forms.PasswordInput(attrs={'class':'form-control'}))