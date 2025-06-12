from django.views.generic.base import TemplateView
from django.shortcuts import render

class HomePageView(TemplateView):
     template_name = "core/home.html"
     def get_context_data(self, **kwargs):
          context = super().get_context_data(**kwargs)
          context['titulo'] = 'Bienvenido a la pagina de la web musical'
          return context


