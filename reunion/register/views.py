from django.shortcuts import render, HttpResponse, redirect
from .forms import RegistroForm
from django.urls import reverse
from django.core.mail import EmailMessage
from django.core.mail import EmailMultiAlternatives
from directores.models import Director, Ut

# Create your views here.
def register(request):
    #print("Tipo de peticion: {}" .format(request.method))

    utlist = Ut.objects.all().order_by('claveUt')


    register_form = RegistroForm()
    if request.method == "POST":
        register_form = RegistroForm(data=request.POST)
        print(register_form.is_valid())
        if register_form.is_valid():

            nombre = request.POST.get("nombre",'')
            apPat = request.POST.get("apPat",'')
            apMat = request.POST.get("apMat",'')
            email = request.POST.get("email",'')
            telefono = request.POST.get("telefono",'')
            grado = request.POST.get("grado",'')
            siglas = request.POST.get("siglas",'')
            clave = request.POST.get("claveUt",'')
            puesto = request.POST.get("puesto",'')

            #guardar
            obj = Director() #gets new object
            obj.nombre = nombre
            obj.apPat = apPat
            obj.apMat = apMat
            obj.correo = email
            obj.telefono = telefono
            obj.grado = grado
            obj.siglas = siglas
            #Esto agregue
            id=Ut.objects.get(claveUt=clave)
            obj.status=0
            obj.claveUt=id
            # hasta aqui
            obj.puesto = puesto
            obj.save()
            
            subject, from_email = 'Registro a la Reunión Naciona de Directores de TIC, Morelia 2018', 'reuniondirectores@gmail.com'
            text_content = ''
            html_content = "<p><p><b>¡Bienvenido {}!</b></p><p></p><p>Tu registro como asistente a la Reunión Nacional de Directores de Tecnologías de la Información y Comunicación de las Universidades Tecnológicas, a realizarse del 10 al 12 de octubre del 2018 ha sido correcto.&nbsp;</p><p></p><p>La recepción y registro de asistencia se llevará a cabo en el día 10 de octubre de 8:30 a 9:30 en las instalaciones del Hotel Best Western Plus, hotel sede de nuestro evento.</p><p></p><b><p align='center'>¡La ciudad de Morelia te espera!</p></b><p align='center'></p><p>Atentamente</p><p><b>MISD. Graciela I. Martínez Avila</b><br> Directora de Carrera de Tecnologías de la Información<br>y Comunicación de la Universidad Tecnológica de Morelia</p><p>443 110 59 85</p>".format(nombre + " " +apPat +" "+ apMat)
            try:
                email = EmailMultiAlternatives(subject, text_content, from_email, [email])
                email.attach_alternative(html_content, "text/html")
                email.send()
                return redirect(reverse('register')+"?ok")
            except:
                return redirect(reverse('register')+"?fail")
    return render(request, "register/register.html",{'form':register_form, 'utlist': utlist})