from django.shortcuts import render
from usuarios.utils.listaEnlazada import ListaEnlazada
from peliculas.utils.listaCircular import listaDobleCircular

# Create your views here.
def index(request):
    peliculas = listaDobleCircular()
    peliculas.CargarXML_LDC(1)
    
    for nodo in peliculas:
        print(nodo.dato.titulo, nodo.dato.imagen)
    
    return render(request, 'main/index.html', {'peliculas': peliculas})

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        lista_usuarios = ListaEnlazada()
        lista_usuarios.CargarXML(1)
        lista_usuarios.login(email, password)
        
        user = lista_usuarios.login(email, password)
        
        if user:
            lista_usuarios.clear
            if user.rol == 'administrador':
                return render(request, 'main/administrador.html')
            elif user.rol == 'cliente':
                return render(request, 'main/cliente.html')
            
        else:
            return render(request, 'main/login.html', {'error': 'Usuario o contraseña incorrectos'})
        
    else:
        return render(request, 'main/login.html')
    
def administrador(request):
    return render(request, 'main/administrador.html')

def cliente(request):
    return render(request, 'main/cliente.html')