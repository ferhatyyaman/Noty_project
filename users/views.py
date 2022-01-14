from django.shortcuts import render

from django.urls import reverse_lazy 
from django.views.generic import CreateView

from .forms import CustomUserCreationForm #forms.py dosyasından import ettik

class SignUpView(CreateView):           # kayıt formu için
    form_class=CustomUserCreationForm 
    success_url=reverse_lazy('login') #basarılı kayıt olunursa login sayfasına git
    template_name='signup.html'





