#-*- coding: utf-8 -*-
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from typing import Any
from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import *
from django.urls import reverse_lazy
# Create your views here., DetailView, 




"""def home(request):
    return render(request, 'home.html', {}) """
@login_required
def LikeView(request, pk):
    article=Article.objects.get(id=pk)
    liked = False
    if article.likes.filter(id=request.user.id).exists():
        article.likes.remove(request.user)
    else:
        article.likes.add(request.user)
        liked=True
    
    return HttpResponseRedirect(reverse('art_detail', args=[str(pk)]))

def approuver_articles(request):
    if request.user.is_staff :
        if request.method == 'POST':
            articles_a_approuver = request.POST.getlist('articles_a_approuver')
            Article.objects.filter(id__in=articles_a_approuver).update(is_online=True)
            return redirect('verif')
        else:
            articles = Article.objects.filter(is_online=False)
            return render(request, 'online.html', {'articles':articles})
    else:
        return redirect('home')
    




def home(request):
    articles= Article.objects.all()
    categories = Categorie.objects.all()
    categorie_comptage = {}
    for  category in categories:
        product_count = Article.objects.filter(categorie = category).count()
        categorie_comptage[category]= product_count
    return render(request, 'home.html', {'categories':categorie_comptage, 'articles': articles })

class ArticleDetailView(DetailView):
    model= Article
    template_name = 'art_detail.html'

    def get_context_data(self, *args,  **kwargs):
        #cat_menu = Categorie.objects.all()
        context = super(ArticleDetailView, self).get_context_data(*args, **kwargs)
        #context['cat_menu']=cat_menu
        stuff = get_object_or_404(Article, id=self.kwargs['pk'])
        total_likes = stuff.total_likes()

        liked=False
        if stuff.likes.filter(id=self.request.user.id).exists():
            liked=True
        
        context['total_likes'] = total_likes 
        context['liked']=liked
        return context

class AddArticleView(LoginRequiredMixin, CreateView):
    model= Article
    form_class= ArticleForm
    template_name='add_article.html'
    #fields= '__all__'

    def form_valid(self, form):
        form.instance.auteur = self.request.user
        form.instance.is_online = False
        return super().form_valid(form)

class AddCategorieView(LoginRequiredMixin, CreateView):
    model= Categorie
    #form_class= CategorieForm
    template_name='add_categorie.html'
    fields= '__all__'


def CategorieView(request, cats):
    categorie_article = Article.objects.filter(categorie = cats.replace('-', ' '))

    return render( request, 'categories.html', {'cats' : cats.title(), 'categorie_article':categorie_article})

class UpdateArticleView(UpdateView, LoginRequiredMixin):
    model=Article
    form_class=EditForm
    template_name='update_art.html'
    #fields = ['titre', 'titre_slug', 'corps']

class DropArticle(DeleteView, LoginRequiredMixin):
    model=Article
    template_name='delete_art.html'
    success_url=reverse_lazy('home')

