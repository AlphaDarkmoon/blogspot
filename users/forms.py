from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser
from django import forms

# Custom form for creating new users, inheriting from UserCreationForm
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        # Specify the fields to be displayed and filled in the form
        fields = ('email','username')
        # Add placeholder attributes for the email input field
        widgets = {
            'email': forms.EmailInput(attrs={'placeholder': "Email address"}),
            'Username': forms.TextInput(attrs={'placeholder': "Username"}),
        }
    
    # Define individual form fields with placeholder attributes
    email = forms.CharField(widget=forms.TextInput(attrs={'placeholder': "Email"}))
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': "Username"}))

    

# Custom form for editing user details, inheriting from UserChangeForm
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        # Specify the fields to be displayed and edited in the form
        fields = ("email","username")
