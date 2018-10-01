from django.shortcuts import render, HttpResponse, redirect
from .forms import RegistroForm
from django.urls import reverse
from django.core.mail import EmailMessage
from directores.models import Director, Ut

# Create your views here.
def register(request):
    #print("Tipo de peticion: {}" .format(request.method))

    utlist = Ut.objects.all().order_by('claveUt')


    register_form = RegistroForm()
    if request.method == "POST":
        register_form = RegistroForm(data=request.POST)
        if register_form.is_valid():
            nombre = request.POST.get("nombre",'')
            apPat = request.POST.get("apPat",'')
            apMat = request.POST.get("apMat",'')
            email = request.POST.get("email",'')
            telefono = request.POST.get("telefono",'')
            grado = request.POST.get("grado",'')
            siglas = request.POST.get("siglas",'')
            claveUt = request.POST.get("claveUt",'')
            puesto = request.POST.get("puesto",'')

            #guardar
            obj = Director() #gets new object
            obj.nombre = nombre
            obj.apPat = apPat
            obj.apMat = apMat
            obj.email = email
            obj.telefono = telefono
            obj.grado = grado
            obj.siglas = siglas

            uts = Ut.objects.filter(claveUt__in=claveUt)
            instance = Director.objects.create(claveUt=claveUt)

            instance.claveUt.set(uts)

            obj.puesto = puesto
            obj.save()

            #suponemos que todo ok redireccinamos y enviamos correo

            email = EmailMessage(
                "Reunión de Directores", 
                "De {} <{}>\n\nEscribió:\n\n{}".format(nombre + " " +apPat +" "+ apMat, email, "Confirmación de regisro"),
                "no-contestar@inbox.gmail.com",
                [email],
                reply_to=[email]
            )
            try:
               
                email.send()
                return redirect(reverse('register')+"?ok")
            except:
                return redirect(reverse('register')+"?fail")
    return render(request, "register/register.html",{'form':register_form, 'utlist': utlist})