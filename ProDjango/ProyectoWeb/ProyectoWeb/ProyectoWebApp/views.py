from django.http import response
from django.shortcuts import render, HttpResponse

# Create your views here.

#Se crea todas las paginas que va a tener el sitio

def home(request):

    return render(request, "ProyectoWebApp/home.html")

def servicios(request):
    
    return render(request, "ProyectoWebApp/servicios.html")

def tienda(request):
    
    return render(request, "ProyectoWebApp/tienda.html")

def blog(request):
    
    return render(request, "ProyectoWebApp/blog.html")

def contacto(request):
    
    return render(request, "ProyectoWebApp/contacto.html")