from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import Post, Category
from .forms import PostForm, UpdatePostForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect

# Class based Views

#########################################################################
#              HomeView to show all of the post titles on index.html    #
#########################################################################

class HomeView(ListView):
    model = Post
    template_name = 'index.html'
    ordering = ['-id','post_time']

    def get_context_data(self,*args, **kwargs):
        cat_values = Category.objects.all()
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context['cat_values'] = cat_values
        return context


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
#              let user update a blog or post using frontend using CreateView              #
############################################################################################

def AdminView(request):
    return render(request, 'admin_templates/admin_index.html')

def CategoryView(request, categories):
    category_posts = Post.objects.filter(category = categories)
    return render(request, 'admin_templates/pages/blogs_related/categories.html', {'categories': categories,'category_posts':category_posts})

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
    
