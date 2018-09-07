from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    return HttpResponse("Inicio")

def register(request):
    return HttpResponse("Registro")

def about(request):
    return HttpResponse("Acerca de")

def program(request):
    return HttpResponse("Programa")

def contact(request):
    return HttpResponse("Contacto")