from django.urls import path
from blogs_app.views import HomeView,ArticleDetailView,AllBlogsView, AddCatagoryView,Addpostview,CategoryView,AdminView, DeletePostView, HomePostView, UpdatePostView, LikeView

app_name = 'blogs_app'

urlpatterns = [
    path ('', HomeView.as_view(), name='home'),
    path('post_list', HomePostView.as_view(), name='post-list'),
    path ('all_blogs', AllBlogsView.as_view(), name='all-blogs'),                                                                                     
    path('article/<int:pk>',ArticleDetailView.as_view(),name = 'articles-page'),        # `pk` referce to primary key #
    path('add_category', AddCatagoryView.as_view(), name='add-category'),
    path('category/<str:categories>', CategoryView, name='category'),
    path('add_blogs', Addpostview.as_view(), name='add-blogs'),
    path('article/<int:pk>/remove', DeletePostView.as_view(), name='delete-blog'),
    path('adminpage', AdminView, name='admin-view'),
    path('article/edit/<int:pk>', UpdatePostView.as_view(), name='update-blog'), 
    path('like/<int:pk>',LikeView, name='like-post'),                                                                                      
]