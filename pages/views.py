from django.views.generic import TemplateView #gömülü templateview import ediyoruz

class HomePageView(TemplateView): #HomePageView sınıfı oluşturduk TemplateView den kalıtım aldırdık
    template_name='home.html'


class hakkında(TemplateView):   
    template_name='hakkında.html'

class iletisim(TemplateView): 
    template_name='iletisim.html'
