from django.urls import path
from .views import HomePageView, ContactPageView

core_patterns = ([
    path('', HomePageView.as_view(), name='home'), 
    path('nosotros/', HomePageView.as_view(), name='nosotros'), 
    path('servicios/', HomePageView.as_view(), name='servicios'), 
    path('trabajos/', HomePageView.as_view(), name='trabajos'), 
    path('blog/', HomePageView.as_view(), name='blog'), 
    path('sobre-nosotros/', HomePageView.as_view(), name='sobre-nosotros'), 
    path('contacto/', ContactPageView.as_view(), name='contacto'), 
    
], "core")
    




