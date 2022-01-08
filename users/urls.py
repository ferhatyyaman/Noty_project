from django.urls import path  #django.urls ten path i import ettik
from .views import SignUpView #views.py deki signupview i import ettik

urlpatterns=[
    path('signup/', SignUpView.as_view(),name='signup'),
    
   
]