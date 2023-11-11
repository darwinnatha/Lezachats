#-*- coding: utf-8 -*-x
from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Article)
admin.site.register(Categorie)
admin.site.register(Profile)