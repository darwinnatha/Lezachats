from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from django import forms


class SignUpForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(max_length=255,widget=forms.TextInput(attrs={'class':'form-control'}))
    numero_de_telephone = forms.NumberInput()
    
    class Meta:
        model= User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1')
        
        def __init__(self, *args, **kwargs):
            super(SignUpForm, self).__init__(*args, **kwargs)
            self.fields['username'].widget.attrs['class'] = 'form-control'
            self.fields['password1'].widget.attrs['class'] = 'form-control'
            self.fields['password2'].widget.attrs['class'] = 'form-control'

class UserUpdateForm(UserChangeForm):
    class Meta:
        model = User
        fields =('username', 'first_name', 'last_name', 'email', 'password')

class PasswordUpdateForm(PasswordChangeForm):
    class Meta:
        model = User
        fields = ('password', 'newpassword1', 'newpassword2')