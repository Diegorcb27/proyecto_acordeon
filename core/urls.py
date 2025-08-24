
from django.urls import path
from .views import HomePageView, ContactoView, GaleryPageView, NosotrosPageView, CursoPageView
core_patterns = ([
    path('', HomePageView.as_view(), name='home'), 
    path('nosotros/', NosotrosPageView.as_view(), name='nosotros'), 
    path('curso/', CursoPageView.as_view(), name='cursos'), 
    path('blog/', HomePageView.as_view(), name='blog'), 
    path('galeria/', GaleryPageView.as_view(), name='galeria'), 
    path('contacto/', ContactoView.as_view(), name='contacto'), 
    
], "core")
    




