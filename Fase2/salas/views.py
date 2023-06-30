import requests
from django.shortcuts import render
from .utils.listaDoble import Lista_Doble
from .utils.salas import Sala

# Create your views here.
def crud_salas(request):
    lista_salas = Lista_Doble()
    lista_salas.CargarXML_LD(1)
    
    response = requests.get('http://localhost:5022/salas')
    rooms_API = response.json()
    print(rooms_API)
    
    for room in rooms_API:
        lista_salas.add(room)
    
    if request.method == 'POST':
        action = request.POST.get('action')
        numero = request.POST.get('numero')
        asientos = request.POST.get('asientos')
        
        objeto = Sala(numero, asientos)
        
        if action == 'add':
            lista_salas.add(objeto)
            lista_salas.agregarXML_LD(numero, asientos)
        elif action == 'modify':
            index = request.POST.get('index')
            lista_salas.modify(objeto, index)
            lista_salas.editarXML_LD(numero, asientos)
        elif action == 'delete':
            lista_salas.delete(objeto)
            lista_salas.eliminarXML_LD(numero)
            
    rooms = []
    current = lista_salas.cabeza
    index = 0
    
    while current is not None:
        rooms.append((index, current.dato))
        current = current.siguiente
        index += 1
    
    return render(request, 'salas/crud_salas.html', {'rooms': rooms})