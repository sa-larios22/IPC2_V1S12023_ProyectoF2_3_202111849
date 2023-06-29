from django.shortcuts import render, redirect
from Usuarios.Clases.listaEnlazada import ListaEnlazada
from Usuarios.Clases.usuarios import Usuario

# Create your views here.
global lista_enlazada
lista_enlazada = ListaEnlazada()

def mostrar_user(request):
    return render(request, 'Usuarios/show_user_admin_menu.html', {'Usuarios': lista_enlazada})

def cargar_xml(request):
    if request.method == 'POST':
        lista_enlazada.CargarXML(1)
    return render(request, 'Usuarios/show_user_admin_menu.html', {'Usuarios':lista_enlazada})

def agregar_usuario(request):
    if request.method == 'POST':
        lista_enlazada.CargarXML(1)
        rol = 'cliente'
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        telefono = request.POST.get('telefono')
        correo = request.POST.get('correo')
        contrasena = request.POST.get('contrasena')
        
        objeto = Usuario(rol, nombre, apellido, telefono, correo, contrasena)
        lista_enlazada.add(objeto)
        
        return redirect('mostrar_user')
    return render(request, 'Usuarios/agregar_usuario.html')