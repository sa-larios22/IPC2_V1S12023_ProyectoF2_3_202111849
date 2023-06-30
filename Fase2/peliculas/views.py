import requests
from django.shortcuts import render
from .utils.listaCircular import listaDobleCircular
from .utils.peliculas import Pelicula

# Create your views here.
def crud_peliculas(request):
    lista_peliculas = listaDobleCircular()
    lista_peliculas.CargarXML_LDC(1)
    
    response = requests.get('http://localhost:5022/peliculas')
    movies_API = response.json()
    print(movies_API)
    
    for movie in movies_API:
        lista_peliculas.add(movie)
    
    if request.method == 'POST':
        action = request.POST.get('action')
        categoria = request.POST.get('categoria')
        titulo = request.POST.get('titulo')
        director = request.POST.get('director')
        anio = request.POST.get('anio')
        fecha = request.POST.get('fecha')
        hora = request.POST.get('hora')
        imagen = request.POST.get('imagen')
        precio = request.POST.get('precio')
        
        objeto = Pelicula(categoria, titulo, director, anio, fecha, hora, imagen, precio)
        
        if action == 'add':
            lista_peliculas.add(objeto)
            lista_peliculas.agregarXML_LDC(categoria, titulo, director, anio, fecha, hora, imagen, precio)
        elif action == 'modify':
            index = request.POST.get('index')
            lista_peliculas.modify(objeto, index)
            lista_peliculas.editarXML_LDC(objeto)
        elif action == 'delete':
            lista_peliculas.delete(objeto)
            lista_peliculas.eliminarXML_LDC(titulo)
            
    movies = []
    current = lista_peliculas.cabeza
    index = 0
    
    if current is not None:
        while True:
            movies.append((index, current.dato))
            current = current.siguiente
            index += 1
            if current == lista_peliculas.cabeza:
                break
    
    return render(request, 'peliculas/crud_peliculas.html', {'movies': movies})

def view_movies(request):
    lista_peliculas = listaDobleCircular()
    titulos = lista_peliculas.get_all_titulos()
    imagenes = lista_peliculas.get_all_imagenes()
    
    movie_list = list(zip(titulos, imagenes))
    
    return render(request, 'peliculas/crud_peliculas.html', {'movie_list': movie_list})