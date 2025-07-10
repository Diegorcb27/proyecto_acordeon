from django.views.generic.base import TemplateView
from django.shortcuts import render
from .forms import ContactForm

class HomePageView(TemplateView):
     template_name = "core/home.html"
    

class ContactPageView(TemplateView):
     template_name = "core/contact.html"
     

from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .forms import ContactForm
from django.conf import settings
from django.views.generic.edit import FormView
from django.contrib import messages

# def contacto(request):
#     form = ContactForm()
#     if request.method == "POST":
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             nombre = form.cleaned_data["nombre"]
#             correo = form.cleaned_data["email"]
#             mensaje = form.cleaned_data["mensaje"]

#             asunto = f"Nuevo mensaje de contacto: {nombre}"
#             contenido = f"Nombre: {nombre}\nEmail: {correo}\nMensaje:\n{mensaje}"

#             send_mail(
#                 asunto,
#                 contenido,
#                 settings.DEFAULT_FROM_EMAIL,
#                 ['diegorbcastro@gmail.com'],  # Cambia por el correo destino
#             )
#             return redirect("contacto_exitoso")

#     return render(request, "core/contact.html", {"form": form})
# from django.views.generic.edit import FormView




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

# from django.core.mail import send_mail
# from django.contrib import messages

# class ContactoView(FormView):
#     template_name = 'core/contact.html'
#     form_class = ContactForm
#     success_url = None

#     def form_valid(self, form):
#         try:
#             # Construye el mensaje incluyendo el correo del remitente
#             mensaje_completo = (
#                 f"Mensaje de: {form.cleaned_data['nombre']}\n"
#                 f"Correo: {form.cleaned_data['email']}\n\n"
#                 f"Mensaje:\n{form.cleaned_data['mensaje']}"
#             )
            
#             send_mail(
#                 subject=f"Nuevo contacto de {form.cleaned_data['nombre']}",
#                 message=mensaje_completo,
#                 from_email='diegorbcastro@gmail.com',  # Tu correo Gmail
#                 recipient_list=['diegorbcastro@gmail.com'],  # Tu correo de destino
#                 reply_to=[form.cleaned_data['email']],  # Correo para responder
#                 fail_silently=False
#             )
#             messages.success(self.request, "¡Mensaje enviado con éxito!")
#         except Exception as e:
#             messages.error(self.request, f"Error al enviar: {str(e)}")
        
#         return self.render_to_response(self.get_context_data(form=form, exito=True))