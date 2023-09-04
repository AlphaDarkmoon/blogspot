from django import forms
from .models import Post, Category

from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User


choices = Category.objects.all().values_list('name','name')   # `name` is from models.py Category class

choice_list = []   # List of category 

for item in choices:
    choice_list.append(item)

class PostForm(forms.ModelForm):            #improve UI using forms.py without html,css | using Bootstrap
    class Meta:
        model = Post
        fields = ('title','title_tag','author','banner_img','category','snippet','body')

        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter title here'}),
            'title_tag': forms.TextInput(attrs={'class':'form-control','placeholder':'Enter title tag here'}),
            'author': forms.Select(attrs={'class':'form-control'}),
            'banner_img': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter Image Link here'}),
            'category': forms.Select(choices=choice_list,attrs={'class':'form-control','placeholder':choices}),
            'snippet': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter snippet here'}),
            'body': forms.Textarea(attrs={'class':'form-control','placeholder':'Enter body here...'}),
        }



class UpdatePostForm(forms.ModelForm):            #improve UI using forms.py without html,css | using Bootstrap
    class Meta:
        model = Post
        fields = ('title','title_tag','banner_img','snippet','body')

        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter title here'}),
            'banner_img': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter Image Link here'}),
            'title_tag': forms.TextInput(attrs={'class':'form-control','placeholder':'Enter title tag here'}),
            'snippet': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter snippet here'}),
            'body': forms.Textarea(attrs={'class':'form-control','placeholder':'Enter body here...','rows': 10}),
        }




# Custom form for creating new users, inheriting from UserCreationForm
class UpdateAdminProfileForm(UserChangeForm):
    class Meta:
        model = User
        # Specify the fields to be displayed and filled in the form
        fields = ("username","email", "first_name", "last_name")
    
    # Define individual form fields with placeholder attributes