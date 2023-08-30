from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

#############################################
#              Creates a model              #
#                    to                     #
#       store post contents from backend    #
#############################################

class Post(models.Model):
    title = models.CharField(max_length=255)
    title_tag = models.CharField(max_length=60, default="tag for title...")
    banner_img = models.CharField(max_length=225, default='https://i.ibb.co/qgbtz4x/black-hole-1.png')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    post_time = models.DateField(auto_now_add = True)

    def __str__(self):
        return self.title + ' | ' + str(self.author)
    
    def get_absolute_url(self):
        # return reverse('articles-page', args = (str(self.id)))  # to redirect to the aritcle page of same post
        return reverse('home')                                    
    


