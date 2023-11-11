from django import forms
from .models import *

choices = Categorie.objects.all().values_list('nom', 'nom')

liste_choix = []

for item in choices:
    liste_choix.append(item)



class ArticleForm(forms.ModelForm):
    class Meta:
        model=Article
        fields = ('image','nom','categorie', 'prix', 'corps')

        widgets={
            'image': forms.FileInput(attrs= {'class':'image-input', 'required': 'required'}),
        }

class EditForm(forms.ModelForm):
    class Meta:
        model=Article
        fields = ('nom', 'categorie', 'prix', 'corps','image')

    
        widgets={
            'image': forms.FileInput(attrs= {'class':'image-input', 'required': 'required'}),
        }