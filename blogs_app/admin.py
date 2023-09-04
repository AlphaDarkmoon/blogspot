from django.contrib import admin
from .models import Post, Category, Profile

# Register your models here.

admin.site.register(Post)  ### Registered the Post model, to know more go to models.py ###
admin.site.register(Category)
admin.site.register(Profile)