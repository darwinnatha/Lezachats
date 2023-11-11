from .views import *
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', home, name='home'),
    path('article/<int:pk>', ArticleDetailView.as_view(), name='art_detail'),
    path('article/add', AddArticleView.as_view(),name='add_art'), 
    path('article/<int:pk>/edit', UpdateArticleView.as_view(), name='edit_art'),
    path('article/<int:pk>/drop', DropArticle.as_view(), name='delete_art'),
    path('category/add', AddCategorieView.as_view(), name='add_cat'),
    path('category/<str:cats>/', CategorieView, name='cats'),
    path('like/<int:pk>', LikeView, name='like_art'),
    path('verif/', approuver_articles, name='verif'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
