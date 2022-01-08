from django.contrib import admin

from django.contrib.auth.admin import UserAdmin             #yeni admin panelini import ettik
from django.contrib.auth.forms import UserCreationForm      #form.py dosyasından yazdığımız formları import ettik

from .forms import CustomUserChangeForm, CustomUserChangeForm 
from .models import CustomUser                               #model.py dosyasında yazdığımız customuseri import ediyoruz

class CustomUserAdmin(UserAdmin):
    add_form=CustomUserChangeForm #form düzenleme
    model= CustomUser
    add_form=UserCreationForm  #form oluşturma
    list_display=['username','email','age','is_staff',] #admin sayfası görünen degerler

admin.site.register(CustomUser,CustomUserAdmin) #model.py de bulunan customuser sınıfını ve admin.py de bulunan customuseradmin sınıfını register ettik