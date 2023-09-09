from django import forms
from .models import Post, Category, Profile

from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User


choices = Category.objects.all().values_list('name','name')   # `name` is from models.py Category class

choice_list = []   # List of category 

for item in choices:
    choice_list.append(item)

class PostForm(forms.ModelForm):            #improve UI using forms.py without html,css | using Bootstrap
    class Meta:
        model = Post
        fields = ('title','title_tag','author','author_name','banner_img','category','snippet','body')

        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter title here'}),
            'title_tag': forms.TextInput(attrs={'class':'form-control','placeholder':'Enter title tag here'}),
            'author': forms.Select(attrs={'class':'form-control'}),
            'author_name': forms.TextInput(attrs={'class':'form-control'}),
            'category': forms.Select(choices=choice_list,attrs={'class':'form-control','placeholder':choices}),
            'snippet': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter snippet here'}),
            'body': forms.Textarea(attrs={'class':'form-control','placeholder':'Enter body here...'}),
        }



class UpdatePostForm(forms.ModelForm):            #improve UI using forms.py without html,css | using Bootstrap
    class Meta:
        model = Post
        fields = ('title','title_tag','author','author_name','banner_img','category','snippet','body')

        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter title here'}),
            'title_tag': forms.TextInput(attrs={'class':'form-control','placeholder':'Enter title tag here'}),
            'author': forms.Select(attrs={'class':'form-control'}),
            'author_name': forms.TextInput(attrs={'class':'form-control'}),
            'category': forms.Select(choices=choice_list,attrs={'class':'form-control','placeholder':choices}),
            'snippet': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter snippet here'}),
            'body': forms.Textarea(attrs={'class':'form-control','placeholder':'Enter body here...'}),
        }




# Custom form for creating new users, inheriting from UserCreationForm
class UpdateAdminProfileForm(UserChangeForm):
    class Meta:
        model = User
        # Specify the fields to be displayed and filled in the form
        fields = ( "username", "email")
    
    # Define individual form fields with placeholder attributes


class PasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','type':'password'}))
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','type':'password'}))
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','type':'password'}))

    class Meta:
        model = User
        fields = ('old_password','new_password1','new_password2')

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'profile_pic',]