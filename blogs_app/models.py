from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.conf import settings

from ckeditor.fields import RichTextField
 

#############################################
#              Creates a model              #
#                    to                     #
#       store post contents from backend    #
#############################################

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, null=True, on_delete = models.CASCADE)
    name = models.CharField(max_length=80,default='name')
    bio = models.CharField(max_length=225)
    profile_pic = models.ImageField(null=True,blank = True, upload_to="images/admin/profile")

    def __str__(self):
        return str(self.user)


class Post(models.Model):
    title = models.CharField(max_length=255)
    title_tag = models.CharField(max_length=60, default="tag for title...")
    banner_img = models.ImageField(null = True, blank=True, upload_to="images/blogs/blogs_banner")
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    author_name = models.CharField(max_length=60, default="...")
    category = models.CharField(max_length=225, default="python")
    snippet = models.CharField(max_length=255)
    body = RichTextField(blank=True,null=True)
    post_time = models.DateField(auto_now_add = True)
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='blog_posts')

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title + ' | ' + str(self.author)
    
    def get_absolute_url(self):
        # return reverse('articles-page', args = (str(self.id)))  # to redirect to the aritcle page of same post
        return reverse('blogs_app:home') 
                                           
    


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('blogs_app:home')

