from django.urls import path
from .views import HomePageView, iletisim ,hakkında #views.py den Homepagevivews import ediyoruz

urlpatterns=[
    path('',HomePageView.as_view(), name='home'),    #sınıf tabanlı view olunca as_view kullanılmalı
    path('hakkında/',hakkında.as_view(), name='hakkında'),
    path('iletisim/',iletisim.as_view(), name='iletisim'),
]