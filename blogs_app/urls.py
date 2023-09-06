from django.urls import path
from blogs_app.views import HomeView,ArticleDetailView,AllBlogsView, AddCatagoryView,Addpostview,CategoryView,AdminView, DeletePostView, HomePostView, UpdatePostView, LikeView,UserEditView, ProfileEditView, ChangePasswordsView, AuthorProfile
from django.contrib.auth import views as auth_views
from . import views

app_name = 'blogs_app'

urlpatterns = [
    path ('', HomeView.as_view(), name='home'),
    path('post_list', HomePostView.as_view(), name='post-list'),
    path ('all_blogs', AllBlogsView, name='all-blogs'),                                                                                     
    path('article/<int:pk>',ArticleDetailView.as_view(),name = 'articles-page'),        # `pk` referce to primary key #
    path('add_category', AddCatagoryView.as_view(), name='add-category'),
    path('category/<str:categories>', CategoryView, name='category'),
    path('add_blogs', Addpostview.as_view(), name='add-blogs'),
    path('article/<int:pk>/remove', DeletePostView.as_view(), name='delete-blog'),
    path('adminpage', UserEditView.as_view(), name='admin-view'),
    path('article/edit/<int:pk>', UpdatePostView.as_view(), name='update-blog'), 
    path('like/<int:pk>',LikeView, name='like-post'),  
    path('1/password/',auth_views.PasswordChangeView.as_view(template_name = 'change_pass.html')),
    path('password/',ChangePasswordsView.as_view(template_name = 'change_pass.html')),     
    path('userprofile',views.update_profile, name = 'user-profile'),  
    # path('author', views.AuthorProfile, name='author'), 
    path ('author', AuthorProfile.as_view(), name='author'),                                                                                 
]