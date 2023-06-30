import requests
from django.shortcuts import render
from .utils.listaDoble import ListaDoble
from .utils.tarjetas import Tarjeta

# Create your views here.
def crud_tarjetas(request):
    lista_tarjetas = ListaDoble()
    lista_tarjetas.CargarXML_LD(1)
    
    response = requests.get('http://localhost:5022/tarjetas')
    cards_API = response.json()
    print(cards_API)
    
    for card in cards_API:
        lista_tarjetas.add(card)
        
    if request.method == 'POST':
        action = request.POST.get('action')
        tipo = request.POST.get('tipo')
        numero = request.POST.get('numero')
        titular = request.POST.get('titular')
        fecha_expiracion = request.POST.get('fecha_expiracion')
        
        objeto = Tarjeta(tipo, numero, titular, fecha_expiracion)
        
        if action == 'add':
            lista_tarjetas.add(objeto)
            lista_tarjetas.agregarXML_LD(tipo, numero, titular, fecha_expiracion)
        elif action == 'modify':
            index = request.POST.get('index')
            lista_tarjetas.modify(objeto, index)
            lista_tarjetas.editarXML_LD(tipo, numero, titular, fecha_expiracion)
        elif action == 'delete':
            lista_tarjetas.delete(objeto)
            lista_tarjetas.eliminarXML_LD(numero)
            
    cards = []
    current = lista_tarjetas.cabeza
    index = 0
    
    while current is not None:
        cards.append((index, current.dato))
        current = current.siguiente
        index += 1
        
    return render(request, 'tarjetas/crud_tarjetas.html', {'cards': cards})