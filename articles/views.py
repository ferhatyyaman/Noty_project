from django.contrib.auth.mixins import LoginRequiredMixin   #yalnızca giriş yapanların view erişimine izin belirleme 
from django.core.exceptions import PermissionDenied #dispatch fonksiyonu için kullandık
from django.db import models
from django.forms import widgets         #not yazarı ile giriş yapan kullanıcı aynı ise düzenleme yapabilecek
from django.views.generic import ListView, DetailView, CreateView  #gömülü view
from django.views.generic.edit import UpdateView, DeleteView	   #gömülü view
from django.urls import reverse_lazy
from .models import Article,Comment  #articles/models ten article sınıfını import ettik



class ArticleListView(LoginRequiredMixin, ListView):
    model = Article
    template_name = "article_list.html"
    login_url='login' 	#giriş yapılmadıysa login sayafasına yönlendirilicek 


class ArticleDetailView(LoginRequiredMixin, DetailView):
    model = Article
    template_name = "article_detail.html"
    login_url='login'


class ArticleUpdateView(LoginRequiredMixin, UpdateView): #güncelleme sınıfı
    model = Article
    fields = ('title', 'body',)                         #güncellenecek alanlar
    template_name = 'article_edit.html'
    login_url = 'login'	
    def dispatch(self, 	request, *args, **kwargs):  #Dispatch fonksiyonu=yalnız makale sahibi değişiklik yapabilir
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied
        return super().dispatch(request,*args, **kwargs)



class ArticleDeleteView(LoginRequiredMixin, DeleteView): #silme sınıfı
    model = Article
    template_name = 'article_delete.html'
    success_url = reverse_lazy('article_list') #silme olduktan sonra yönlendirilecek sayfa
    login_url = 'login'	
    def dispatch(self, request, *args, **kwargs): #Dispatch fonksiyonu=yalnız makale sahibi değişiklik yapabilir
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)



class ArticleCreateView(LoginRequiredMixin, CreateView): # oluşturma sınıfı
    
    model = Article
    template_name = "article_new.html"
    fields=('title','body')
    login_url='login'

    

    def form_valid(self, form):                 #yetki ve izin işlemleri
        form.instance.author=self.request.user  #aktif kullanıcıya göre not paylaşan ismini atama yapar         
        return super().form_valid(form)




class CommentCreateView(LoginRequiredMixin,CreateView): # oluşturma sınıfı
    
    model = Comment
    template_name = "comment_new.html"
    fields=('article','comment')
    success_url = reverse_lazy('article_list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


    
    
    
