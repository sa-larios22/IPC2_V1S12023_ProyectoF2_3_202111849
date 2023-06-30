from django.shortcuts import render
from .utils.listaDoble import Lista_Doble
from .utils.salas import Sala

def crud_salas(request):
    lista_salas = Lista_Doble()
    lista_salas.CargarXML_LD(1)
    
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