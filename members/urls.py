from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views 

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('profile/<int:pk>/edit/', UserEditView.as_view(), name='edit_profile'),
    path('profile/<int:pk>/password/', auth_views.PasswordChangeView.as_view(template_name='registration/change-password.html')),
    path('password_success', password_success, name='password_success'),
    path('profile/<int:pk>', ShowProfilePageView.as_view(), name='profile_page')

]