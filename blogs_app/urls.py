from django.urls import path
from blogs_app.views import HomeView,ArticleDetailView,AllBlogsView

app_name = 'blogs_app'

urlpatterns = [
    path ('', HomeView.as_view(), name='home'),
    path ('all_blogs', AllBlogsView.as_view(), name='all-blogs'),                                                                                     
    path('article/<int:pk>',ArticleDetailView.as_view(),name = 'articles-page'),        # `pk` referce to primary key #
                                                                                        
]