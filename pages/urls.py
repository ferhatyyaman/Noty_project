from django.urls import path
from django.views.generic.base import View
from .views import HomePageView, iletisim ,hakkında #views.py den Homepagevivews import ediyoruz

urlpatterns=[
    path('',HomePageView.as_view(), name='home'),
    path('hakkında/',hakkında.as_view(), name='hakkında'),
    path('iletisim/',iletisim.as_view(), name='iletisim'),
]