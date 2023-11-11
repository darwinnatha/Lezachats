from typing import Any
from django.shortcuts import render, get_object_or_404
from django.views.generic import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.urls import reverse_lazy
from .forms import *
from main.models import *
class EditProfileView(UpdateView):
    model=Profile
    template_name = 'registration/edit_profile.html'
    fields=['bio', 'pp', 'website_url', 'fb_url', 'twitter_url', 'numero_de_telephone']
    success_url = reverse_lazy('home')

class ShowProfilePageView(DetailView):
    model=Profile
    template_name = 'registration/user_profile.html'
    
    def get_context_data(self, *args,  **kwargs):
        #cat_menu = Categorie.objects.all()
        users=Profile.objects.all()
        context = super(ShowProfilePageView, self).get_context_data(*args, **kwargs)
        #context['cat_menu']=cat_menu
        page_user = get_object_or_404(Profile, id=self.kwargs['pk'])
        user = self.object.user
        articles = Article.objects.filter(auteur=user)
        context['utilis']=user
        context['page_user']=page_user
        context['articles'] = articles
        return context

class UserRegisterView(CreateView, LoginRequiredMixin):
    form_class=SignUpForm
    template_name='registration/register.html'
    success_url=reverse_lazy('login')
    
    def form_valid(self, form):
        form.instance.is_staff = False
        return super().form_valid(form)
    
@login_required
def password_success(request):
    return render(request, 'password_success.html', )

class UserEditView(UpdateView, LoginRequiredMixin):
    #form_class=UserChangeForm
    template_name='registration/edit_profile.html'
    form_class= UserUpdateForm
    success_url=reverse_lazy('home')

    def get_object(self, ):
        return self.request.user

class PasswordUpdateView(LoginRequiredMixin, PasswordChangeView):
    form_class = PasswordUpdateForm
    template_name = 'registration/change-password.html'
    success_url = reverse_lazy('home')