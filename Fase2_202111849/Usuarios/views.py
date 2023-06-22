from django.shortcuts import render
from Usuarios.Clases.listaEnlazada import ListaEnlazada

# Create your views here.
global lista_enlazada
lista_enlazada = ListaEnlazada()

def mostrar_user(request):
    return render(request, 'Usuarios/show_user_admin_menu.html', {'Usuarios': lista_enlazada})

def cargar_xml(request):
    if request.method == 'POST':
        lista_enlazada.CargarXML(1)
    return render(request, 'Usuarios/show_user_admin_menu.html', {'Usuarios':lista_enlazada})