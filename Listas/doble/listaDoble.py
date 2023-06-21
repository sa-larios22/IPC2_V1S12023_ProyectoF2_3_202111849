import xml.etree.ElementTree as ET
from Listas.doble.nodoDoble import Nodo
from clases.salas import Sala

class Lista_Doble:
    def __init__(self):
        self.cabeza = None

    def add(self, dato):
        nuevo_nodo = Nodo(dato)

        if self.cabeza is None:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza

            while actual.siguiente is not None:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo
            nuevo_nodo.anterior = actual

    def modify(self, dato_nuevo, index):
        actual = self.cabeza
        indice = 0

        while actual is not None:
            if indice == index:
                actual.dato = dato_nuevo
                return
            indice += 1
            actual = actual.siguiente

    def delete(self, dato):
        if self.cabeza is None:
            return

        if self.cabeza.dato == dato:
            self.cabeza = self.cabeza.siguiente
            if self.cabeza is not None:
                self.cabeza.anterior = None
            return

        actual = self.cabeza
        while actual.siguiente is not None:
            if actual.siguiente.dato == dato:
                break
            actual = actual.siguiente

        if actual.siguiente is None:
            return

        if actual.siguiente.siguiente is None:
            actual.siguiente = None
        else:
            actual.siguiente = actual.siguiente.siguiente
            actual.siguiente.anterior = actual

    def search(self, numero):
        actual = self.cabeza
        while actual:
            if actual.dato.numero == numero:
                return actual.dato
            actual = actual.siguiente
        return None

    def Imprimir_LD(self):
        actual = self.cabeza
        actual.dato.imprimir()
        while actual.siguiente is not None:
            actual = actual.siguiente
            actual.dato.imprimir()

    def CargarXML_LD(self, operacion):
        
        tree = ET.parse('Archivos de Entrada\\salas.xml')
        root = tree.getroot()

        for cine in root.findall('cine'):
            for salas in cine.findall('salas'):
                for indice, sala in enumerate(salas.findall('sala')):

                    numero = sala.find('numero').text
                    asientos = sala.find('asientos').text

                    objeto = Sala(numero, asientos)

                    if operacion == 1: # agregar datos a lista
                        self.add(objeto)
                    elif operacion == 2:
                        self.modify(objeto, indice)
                    elif operacion == 3:
                        self.delete(objeto)

    def editarXML_LD(self, tmp_numero, new_asientos):
        tree = ET.parse('Archivos de Entrada\\salas.xml')
        root = tree.getroot()

        for cine in root.findall('cine'):
            for salas in cine.findall('salas'):
                for sala in salas.findall('sala'):
                    if sala.find('numero').text == tmp_numero:
                        asientos = sala.find('asientos')
                        asientos.text = new_asientos
                        break
        
        tree.write('Archivos de Entrada\\salas.xml')

        self.cabeza = None
        self.CargarXML_LD(1)

    def eliminarXML_LD(self, tmp_numero):
        tree = ET.parse('Archivos de Entrada\\salas.xml')
        root = tree.getroot()

        for cine in root.findall('cine'):
            for salas in cine.findall('salas'):
                for sala in salas.findall('sala'):
                    if sala.find('numero').text == tmp_numero:
                        salas.remove(sala)
                        break

        tree.write('Archivos de Entrada\\salas.xml')

        self.CargarXML_LD(3)