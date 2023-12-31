import requests
from django.shortcuts import render
from .utils.listaEnlazada import ListaEnlazada
from .utils.usuarios import Usuario

# Create your views here.
def crud_usuarios(request):
    lista_usuarios = ListaEnlazada()
    lista_usuarios.CargarXML(1)
    
    response = requests.get('http://localhost:5022/usuarios')
    users_API = response.json()
    print(users_API)
    
    for user in users_API:
        lista_usuarios.add(user)
    
    if request.method == 'POST':
        action = request.POST.get('action')
        rol = request.POST.get('rol')
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        telefono = request.POST.get('telefono')
        correo = request.POST.get('correo')
        contrasena = request.POST.get('contrasena')
        
        objeto = Usuario(rol, nombre, apellido, telefono, correo, contrasena)
        
        if action == 'add':
            lista_usuarios.add(objeto)
            lista_usuarios.agregarXML(rol, nombre, apellido, telefono, correo, contrasena)
        elif action == 'modify':
            index = request.POST.get('index')
            lista_usuarios.modify(objeto, index)
            lista_usuarios.editarXML(rol, nombre, apellido, telefono, correo, contrasena)
        elif action == 'delete':
            lista_usuarios.delete(objeto)
            lista_usuarios.eliminarXML(correo)
    
    users = []
    current = lista_usuarios.cabeza
    index = 0

    while current is not None:
        users.append((index, current.dato))
        current = current.siguiente
        index += 1
    
    return render(request, 'usuarios/crud_usuarios.html', {'users': users})