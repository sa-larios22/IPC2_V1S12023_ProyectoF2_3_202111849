import xml.etree.ElementTree as ET
from .nodoDoble import Nodo
from .salas import Sala
import os

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
        script_dir = os.path.dirname(__file__)
        xml_file_path = os.path.join(script_dir, 'salas.xml')
        tree = ET.parse(xml_file_path)
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

    def agregarXML_LD(self, numero, asientos):
        script_dir = os.path.dirname(__file__)
        xml_file_path = os.path.join(script_dir, 'salas.xml')
        tree = ET.parse(xml_file_path)
        root = tree.getroot()
        
        elemento_salas = root.find('cine/salas')
        new_sala = ET.SubElement(elemento_salas, 'sala')
        ET.SubElement(new_sala, 'numero').text = numero
        ET.SubElement(new_sala, 'asientos').text = asientos
        
        self.indent_salas(root)
        
        try:
            tree.write(xml_file_path)
        except Exception as e:
            print(e)

    def editarXML_LD(self, tmp_numero, new_asientos):
        script_dir = os.path.dirname(__file__)
        xml_file_path = os.path.join(script_dir, 'salas.xml')
        tree = ET.parse(xml_file_path)
        root = tree.getroot()

        for cine in root.findall('cine'):
            for salas in cine.findall('salas'):
                for sala in salas.findall('sala'):
                    if sala.find('numero').text == tmp_numero:
                        asientos = sala.find('asientos')
                        asientos.text = new_asientos
                        break
                    
        self.eliminarXML_LD(tmp_numero)
        
        tree.write(xml_file_path)

        self.cabeza = None

    def eliminarXML_LD(self, tmp_numero):
        script_dir = os.path.dirname(__file__)
        xml_file_path = os.path.join(script_dir, 'salas.xml')
        tree = ET.parse(xml_file_path)
        root = tree.getroot()

        for cine in root.findall('cine'):
            for salas in cine.findall('salas'):
                for sala in salas.findall('sala'):
                    if sala.find('numero').text == tmp_numero:
                        salas.remove(sala)
                        break

        tree.write(xml_file_path)
        
    def indent_salas(self, elem, level=0):
        i = "\n" + level*"  "
        if len(elem):
            if not elem.text or not elem.text.strip():
                elem.text = i + "  "
            if not elem.tail or not elem.tail.strip():
                elem.tail = i
            for elem in elem:
                self.indent_salas(elem, level+1)
            if not elem.tail or not elem.tail.strip():
                elem.tail = i
        else:
            if level and (not elem.tail or not elem.tail.strip()):
                elem.tail = i