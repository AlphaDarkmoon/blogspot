from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import Post, Category,Profile
from .forms import PostForm, UpdatePostForm, UpdateAdminProfileForm, PasswordChangeForm,ProfileUpdateForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.views import generic
from django.db.models import Q

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger, Page

# Class based Views

#########################################################################
#              HomeView to show all of the post titles on index.html    #
#########################################################################

import random  # Import the random module



from django.db.models import Count  # Import Count to use in aggregation
from .models import Post, Category

class HomeView(ListView):
    model = Post
    template_name = 'index.html'
    context_object_name = 'recent_posts'
    ordering = ['-id', 'post_time']  # Order posts by post_time in descending order

    def get_context_data(self, *args, **kwargs):
        cat_values = Category.objects.all()
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context['cat_values'] = cat_values

        # Get the 5 most-liked posts with their like counts
        top_liked_posts = Post.objects.annotate(like_count=Count('likes')).order_by('-like_count')[:5]
        context['top_liked_posts'] = top_liked_posts

        # Get all posts and shuffle them
        all_posts = list(Post.objects.all())
        random.shuffle(all_posts)

        # Select the first 5 shuffled items
        context['random_posts'] = all_posts[:5]

        return context



#########################################################################
#              HomeView to show all of the post titles on index.html    #
#########################################################################


# class AllBlogsView(ListView):
#     model = Post
#     template_name = 'all_blogs.html'
#     context_object_name = 'posts'  # Change this to 'posts'
#     ordering = ['-id', 'post_time']
#     paginate_by = 5  # Set the number of items per page


############################################################################################
#              HomeView to show all of the post content in detail on postpage.html.html    #
############################################################################################

class ArticleDetailView(DetailView):
    model = Post
    template_name='blogs.html'

    def get_context_data(self,*args, **kwargs):
        cat_values = Category.objects.all()
        context = super(ArticleDetailView, self).get_context_data(*args, **kwargs)

        stuff = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = stuff.total_likes()

        liked = False
        if stuff.likes.filter(id=self.request.user.id).exists():
            liked=True
        
        context['liked'] = liked
        context['total_likes'] = total_likes
        return context
    


############################################################################################
#              let user add categories using frontend using CreateView                     #
############################################################################################


class AddCatagoryView(CreateView):
    model = Category
    template_name = "admin_templates/pages/blogs_related/add_category.html"
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context

############################################################################################
#              let user add a blog or post using frontend using CreateView                 #
############################################################################################

class Addpostview(CreateView):
    model = Post

    form_class = PostForm       # UI related tags from forms.py
    template_name = 'admin_templates/pages/blogs_related/add_posts.html'






#########################################################################
#              HomeView to show all of the post titles on index.html    #
#########################################################################


class HomePostView(ListView):
    model = Post

    template_name = 'admin_templates/pages/blogs_related/post_list.html'
    ordering = ['-id', 'post_time']



############################################################################################
#              let user update a blog or post using frontend using CreateView              #
############################################################################################


class UpdatePostView(UpdateView):
    model = Post
    form_class = UpdatePostForm
    template_name = "admin_templates/pages/blogs_related/update_posts.html"



############################################################################################
#              let user update a blog or post using frontend using CreateView              #
############################################################################################

class DeletePostView(DeleteView):
    model = Post
    template_name = "admin_templates/pages/blogs_related/delete_post.html"
    success_url = reverse_lazy('blogs_app:admin-view')



############################################################################################
#              let admin update user profile using frontend using CreateView               #
############################################################################################

class UserEditView(generic.UpdateView):  # Edit admin Profile
    form_class = UpdateAdminProfileForm
    template_name= 'admin_templates/admin_index.html'
    success_url = reverse_lazy('blogs_app:home')

    def get_object(self):
            return self.request.user
    

class ProfileEditView(generic.UpdateView):  
    form_class = UpdateAdminProfileForm
    template_name= 'user_profile.html'
    success_url = reverse_lazy('blogs_app:home')

    def get_object(self):
            return self.request.user


class ChangePasswordsView(PasswordChangeView):
    from_class = PasswordChangeForm
    success_url = reverse_lazy('blogs_app:home')

############################################################################################
#              let user update a blog or post using frontend using CreateView              #
############################################################################################

def AdminView(request):
    return render(request, 'admin_templates/admin_index.html')


def AllBlogsView(request):
    search_query = request.GET.get('q')
    if search_query:
        category_posts = Post.objects.filter(
            Q(title__icontains=search_query) |
            Q(category__icontains=search_query) |
            Q(snippet__icontains=search_query)
        )
    else:
        all_posts = Post.objects.all()
        paginator = Paginator(all_posts, 5)
        page = request.GET.get('page')
        category_posts = paginator.get_page(page)
    
    return render(request, 'all_blogs.html', {'category_posts': category_posts, 'search_query': search_query})


def CategoryView(request, categories):
    category_posts = Post.objects.filter(category=categories)
    paginator = Paginator(category_posts, 4)  # Show 4 posts per page

    page = request.GET.get('page')
    category_posts = paginator.get_page(page)

    return render(request, 'admin_templates/pages/blogs_related/categories.html', {'categories': categories, 'category_posts': category_posts})



def LikeView(request,pk):
    post = get_object_or_404(Post,id=request.POST.get('post_id'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True

    return HttpResponseRedirect(reverse('blogs_app:articles-page',args=[str(pk)]))
    
# def AuthorProfile(request):
#     model = Post
#     template_name = 'index.html'
#     ordering = ['-id','post_time']
#     return render(request, 'authorProfile.html')

class AuthorProfile(ListView):
    model = Post
    template_name = 'authorProfile.html'
    ordering = ['-id','post_time']


def update_profile(request):
    profile = request.user.profile  # Get the user's profile
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('blogs_app:home')  # Replace 'profile' with the name of your profile view
    else:
        form = ProfileUpdateForm(instance=profile)
    
    return render(request, 'user_profile.html', {'form': form})
