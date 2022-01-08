from django.db import models
from django.contrib.auth.models import AbstractUser  #abstractuser i import ettik


class CustomUser (AbstractUser):    #ilk custom alanı age
    age=models.PositiveIntegerField( null=True, blank=True) #null ve blank alanın boş geçilmesine olanak sağlar


#null= veritabanı için kullanılır ve true ise değeri olmyan veri saklanır.  blank= onaylama için kullanılır