from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post


# Class based Views

#########################################################################
#              HomeView to show all of the post titles on index.html    #
#########################################################################

class HomeView(ListView):
    model = Post
    template_name = 'index.html'
    ordering = ['-id','post_time']


#########################################################################
#              HomeView to show all of the post titles on index.html    #
#########################################################################

class AllBlogsView(ListView):
    model = Post
    template_name = 'all_blogs.html'
    ordering = ['-id','post_time']




############################################################################################
#              HomeView to show all of the post content in detail on postpage.html.html    #
############################################################################################

class ArticleDetailView(DetailView):
    model = Post
    template_name='blogs.html'