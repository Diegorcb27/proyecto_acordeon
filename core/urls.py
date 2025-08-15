from django.urls import path
from .views import HomePageView, ContactoView, GaleryPageView, NosotrosPageView

core_patterns = ([
    path('', HomePageView.as_view(), name='home'), 
    path('nosotros/', NosotrosPageView.as_view(), name='nosotros'), 
    path('servicios/', HomePageView.as_view(), name='servicios'), 
    path('trabajos/', HomePageView.as_view(), name='trabajos'), 
    path('blog/', HomePageView.as_view(), name='blog'), 
    path('galeria/', GaleryPageView.as_view(), name='galeria'), 
    path('contacto/', ContactoView.as_view(), name='contacto'), 
    # path('contacto/', contacto, name='contacto'), 
    
], "core")
    




