from django.views.generic.base import TemplateView

from .forms import ContactForm

class HomePageView(TemplateView):
    template_name = "core/home.html"
    

class ContactPageView(TemplateView):
    template_name = "core/contact.html"
     


from django.core.mail import send_mail
from django.views.generic.edit import FormView
from django.contrib import messages
from django.shortcuts import render


#enviar correo con formulario de contacto
class ContactoView(FormView):
    template_name = 'core/contact.html'
    form_class = ContactForm
    success_url = None

    def form_valid(self, form):
        try:
          #     Construye el mensaje incluyendo el correo del remitente
            mensaje_completo = (
                f"Mensaje de: {form.cleaned_data['nombre']}\n"
                f"Correo: {form.cleaned_data['email']}\n\n"
                f"Mensaje:\n{form.cleaned_data['mensaje']}"
            )
            
            send_mail(
                subject=f"Nuevo contacto de {form.cleaned_data['nombre']}",
                message=mensaje_completo,
                from_email='diegorbcastro@gmail.com',  # O 'correo' si elegiste la Opción 2
                recipient_list=['diegoramses@hotmail.es', 'diegorbcastro@gmail.com', "theaccordionacademy@gmail.com"], #aqui puedes poner el correo al que quieres enviar el mensaje
                fail_silently=False
            )
            messages.success(self.request, "¡Mensaje enviado con éxito!")
            print("Datos del formulario:", form.cleaned_data)  # Verifica en consola qué datos llegan
        except Exception as e:
            messages.error(self.request, f"Error al enviar: {str(e)}")
        
        return self.render_to_response(self.get_context_data(form=form, exito=True))

class GaleryPageView(TemplateView):
    template_name = "core/galeria.html"
    
class NosotrosPageView(TemplateView):
    template_name = "core/nosotros.html"
    
    
    
    
    
class CursoPageView(TemplateView):
    template_name = "core/cursos.html"
    
    
    
    

    