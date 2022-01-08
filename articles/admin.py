from django.contrib import admin

from .models import Article, Comment #models.py dosyasından article sınıfını import ediyoruz


class CommentInline(admin.TabularInline):
    model=Comment

class ArticleAdmin(admin.ModelAdmin):
    inlines=[
        CommentInline,
     ]

admin.site.register(Article, ArticleAdmin) #not 

admin.site.register(Comment) #yorum
