from django.urls import path
from .views import (ArticleListView,  #articles/view import ettik
                    ArticleUpdateView,  #not güncelleme
                    ArticleDetailView,  
                    ArticleDeleteView,  #not silme
                    ArticleCreateView,  #not oluşturma
                    )

urlpatterns=[
    path('<int:pk>/edit/',ArticleUpdateView.as_view(), name='article_edit'), # not güncelleme yolu girdik
    path('<int:pk>/',ArticleDetailView.as_view(), name='article_detail'), 
    path('<int:pk>/delete/',ArticleDeleteView.as_view(), name='article_delete'), #not silme yolu girdik
    path('new/', ArticleCreateView.as_view(), name='article_new'),           #not oluşturma yolu girdik
    path('',ArticleListView.as_view(), name='article_list'),
]