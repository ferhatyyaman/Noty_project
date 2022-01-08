from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from django.urls import reverse

class Article(models.Model):                   #Metin sınıfı 
    title = models.CharField(max_length=250, verbose_name='Başlık')         #not girilen yerin başlığı
    body = models.TextField(verbose_name='Metin')                           #not girilen yer
    date= models.DateField( auto_now_add=True, verbose_name='Tarih')        #otomatik zaman ve tarih
    author= models.ForeignKey(get_user_model(), on_delete=models.CASCADE,   #Yazar kısmı
        verbose_name='Yazar')

    def __str__(self):  #nesnelerin ismi otomatik yazılacak 
        return self.title

    def get_absolute_url(self):    #yazar alanı setting alanından tanımladığımız custom_user
        return reverse("article_detail", kwargs={"pk": self.pk})

class Comment(models.Model):                    #yorum sınıfı
    article=models.ForeignKey(Article, 
                               verbose_name=("Not"), 
                               on_delete=models.CASCADE,
                               related_name='comments')
    comment=models.CharField(max_length=160, verbose_name=("Yorum") )
    author= models.ForeignKey(get_user_model(), verbose_name=("Yazar"), on_delete=models.CASCADE)

    def __str__(self):
         return self.comment
    
    def get_absolute_url():  #yorumdan sonra notların olduğu sayfaya yönlendiriliyor
         return reverse('article_list')
