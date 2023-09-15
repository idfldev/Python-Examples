from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from .models import Task


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


"""

# class MyForm(forms.ModelForm):
#     class Meta:
#         model = User
#         widgets = {
#             'myfield': forms.TextInput(attrs={'class': 'myfieldclass'}),
#         }

# class LoginForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ("username", "password")

#         widgets = {
#             'username' : forms.TextInput(attrs={'class': 'form-control', 'placeholder' : "name@idfl.com"}),
#             'password' : forms.TextInput(attrs={'class': 'form-control', 'placeholder' : "idfl password"}),
#         }
# ):
#     your_name = forms.CharField(label="Your name", max_length=100)
    

# class UserForm(forms.ModelForm):
#     password = forms.CharField(widget=forms.PasswordInput())
#     class Meta:
#         model = User
#         fields = ('username', 'email', 'password')
#     def __init__(self, *args, **kwargs):
#         super(UserForm,self).__init__(*args,**kwargs)
#         self.fields['username'].widget.attrs.update({'class':'form-control','placeholder':'Username'})
#         self.fields['email'].widget.attrs.update({'class':'form-control','placeholder':'Email'})
#         self.fields['password'].widget.attrs.update({'class':'form-control','placeholder':'Password'})

"""