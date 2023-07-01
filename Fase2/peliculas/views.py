import requests
from django.shortcuts import render
from .utils.listaCircular import listaDobleCircular
from .utils.peliculas import Pelicula

# Create your views here.
def crud_peliculas(request):
    lista_peliculas = listaDobleCircular()
    lista_peliculas.empty()
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

def favoritas(request):
    favoritas = []
    lista_peliculas = listaDobleCircular()
    lista_peliculas.empty()
    lista_peliculas.CargarXML_LDC(1)
    
    response = requests.get('http://localhost:5022/peliculas')
    movies_API = response.json()
    
    for movie in movies_API:
        lista_peliculas.add(movie)
    
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
            
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        # Search for the movie in the list of all movies
        for _, movie in movies:
            if movie.titulo == titulo:
                favoritas.append(movie)
                break


    
    return render(request, 'peliculas/favoritas.html', {'movies': movies, 'favoritas': favoritas})