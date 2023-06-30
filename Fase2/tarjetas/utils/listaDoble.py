import os
import xml.etree.ElementTree as ET
from .nodoDoble import Nodo
from .tarjetas import Tarjeta

class ListaDoble:
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
    
    def CargarXML_LD(self, operacion):
        script_dir = os.path.dirname(__file__)
        xml_file_path = os.path.join(script_dir, 'tarjetas.xml')
        tree = ET.parse(xml_file_path)
        root = tree.getroot()

        for indice, tarjeta in enumerate(root.findall('tarjeta')):
            tipo = tarjeta.find('tipo').text
            numero = tarjeta.find('numero').text
            titular = tarjeta.find('titular').text
            fecha_expiracion = tarjeta.find('fecha_expiracion').text

            objeto = Tarjeta(tipo, numero, titular, fecha_expiracion)

            if operacion == 1: # agregar datos a lista
                self.add(objeto)
            elif operacion == 2:
                self.modify(objeto, indice)
            elif operacion == 3:
                self.delete(objeto)

    def agregarXML_LD(self, tipo, numero, titular, fecha_expiracion):
        script_dir = os.path.dirname(__file__)
        xml_file_path = os.path.join(script_dir, 'tarjetas.xml')
        tree = ET.parse(xml_file_path)
        root = tree.getroot()
        
        new_tarjeta = ET.SubElement(root, 'tarjeta')
        ET.SubElement(new_tarjeta, 'tipo').text = tipo
        ET.SubElement(new_tarjeta, 'numero').text = numero
        ET.SubElement(new_tarjeta, 'titular').text = titular
        ET.SubElement(new_tarjeta, 'fecha_expiracion').text = fecha_expiracion
        
        self.indent_tarjetas(root)
        
        try:
            tree.write(xml_file_path)
        except Exception as e:
            print(e)

    def editarXML_LD(self, tmp_numero, new_tipo, new_titular, new_fecha_expiracion):
        script_dir = os.path.dirname(__file__)
        xml_file_path = os.path.join(script_dir, 'tarjetas.xml')
        tree = ET.parse(xml_file_path)
        root = tree.getroot()

        for tarjeta in root.findall('tarjeta'):
            if tarjeta.find('numero').text == tmp_numero:
                tarjeta.find('tipo').text = new_tipo
                tarjeta.find('titular').text = new_titular
                tarjeta.find('fecha_expiracion').text = new_fecha_expiracion
                break

        self.eliminarXML_LD(tmp_numero)
        tree.write(xml_file_path)
        self.cabeza = None

    def eliminarXML_LD(self, tmp_numero):
        script_dir = os.path.dirname(__file__)
        xml_file_path = os.path.join(script_dir, 'tarjetas.xml')
        tree = ET.parse(xml_file_path)
        root = tree.getroot()

        for tarjeta in root.findall('tarjeta'):
            if tarjeta.find('numero').text == tmp_numero:
                root.remove(tarjeta)
                break

        tree.write(xml_file_path)

    def indent_tarjetas(self, elem, level=0):
        i = "\n" + level*"  "
        if len(elem):
            if not elem.text or not elem.text.strip():
                elem.text = i + "  "
            if not elem.tail or not elem.tail.strip():
                elem.tail = i
            for elem in elem:
                self.indent_tarjetas(elem, level+1)
            if not elem.tail or not elem.tail.strip():
                elem.tail = i
        else:
            if level and (not elem.tail or not elem.tail.strip()):
                elem.tail = i
