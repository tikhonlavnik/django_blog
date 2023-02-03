from django.urls import path
from .views import ArticleView, CategoryView, CreateArticleView


urlpatterns = [
    path('posts/<slug:article_slug>/', ArticleView.as_view(), name='article'),
    path('categories/<slug:category_slug>/', CategoryView.as_view(), name='category'),
    path('addarticle/', CreateArticleView.as_view(), name='addarticle'),
]
