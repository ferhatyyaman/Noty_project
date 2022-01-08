from django import forms #django forms u import ettik

from django.contrib.auth.forms import UserCreationForm, UserChangeForm  #oluşturma ve değiştirme formlarını import ettik

from .models import CustomUser # model.py den custom userı import ettik

class CustomUserCreationForm(UserCreationForm): 
    class Meta(UserCreationForm.Meta):
        model=CustomUser
        fields=('username','email','age') # admin sayfasındaki kullanıcı özellikleri

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model=CustomUser
        fields=('username','email','age')
        