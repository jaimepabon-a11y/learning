from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

@login_required
def contacto(request):
    if request.method == 'POST':
        mensaje = request.POST.get('mensaje')

        try:
            # Envia el correo usando tus credenciales de Gmail fijadas en settings
            send_mail(
                subject=f"Nnova Learning - Nuevo mensaje de {request.user.username}",
                message=f"El usuario {request.user.username} ({request.user.email}) ha enviado el siguiente mensaje desde la plataforma:\n\n{mensaje}",
                from_email=settings.EMAIL_HOST_USER,      # valentina10solano@gmail.com
                recipient_list=[settings.EMAIL_HOST_USER], # Te llegará a ti misma para que lo leas
                fail_silently=False                        # Ponlo en False para capturar si Gmail rechaza la conexión
            )
            messages.success(request, "¡Tu mensaje ha sido enviado con éxito y llegará al correo!")
            
        except Exception as e:
            # Si Google bloquea la IP de Railway o rechaza la clave, no tumba la página, te avisa el error exacto
            print(f"❌ ERROR SMTP DE GMAIL: {e}")
            messages.error(request, f"El mensaje no pudo salir por un problema de autenticación con Gmail.")

        return redirect('contacto')

    return render(request, 'contacto.html')