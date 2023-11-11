from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
from django.forms import FileInput
from django.core.validators import RegexValidator
from phonenumber_field.modelfields import PhoneNumberField
#from ckeditor.fields import RichTextField
# Create your models here.

class Categorie(models.Model):
    nom = models.CharField(max_length=255)

    def __str__(self):
        return self.nom
    def get_absolute_url(self):
        return reverse("home")

class Article(models.Model):
    image = models.ImageField(upload_to='images/',null=True, blank=True)
    nom = models.CharField(max_length=255)
    auteur = models.ForeignKey(User, on_delete=models.CASCADE)
    corps = models.TextField()
    prix=models.IntegerField()
    date = models.DateField(auto_now=False, auto_now_add=True)
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name='blog_likes')
    is_online = models.BooleanField()

    def total_likes(self):
        return self.likes.count()
    
    def __str__(self):
        return self.nom+' |  '+str(self.auteur)
    
    def get_absolute_url(self):
        return reverse('art_detail', args=str(self.pk))

class Profile(models.Model):
    user = models.OneToOneField(User,null=True, on_delete=models.CASCADE)
    bio = models.TextField()
    pp = models.ImageField(upload_to='images/profile/', null=True, blank=True)
    website_url = models.CharField(max_length=255, null=True, blank=True)
    fb_url = models.CharField(max_length=255, null=True, blank=True)
    twitter_url = models.CharField(max_length=255, null=True, blank=True)
    numero_de_telephone = PhoneNumberField(region='CM', unique=True, blank=False, null=False)
    
    def __str__(self):
        return str(self.user)

    def get_absolute_url(self):
        return reverse("profile_page", kwargs={"pk": self.pk})
