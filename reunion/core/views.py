from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, "core/home.html")

def register(request):
    return render(request, "core/register.html")

def about(request):
    return render(request, "core/about.html")

def program(request):
    return render(request, "core/program.html")

def contact(request):
    return render(request, "core/contact.html")