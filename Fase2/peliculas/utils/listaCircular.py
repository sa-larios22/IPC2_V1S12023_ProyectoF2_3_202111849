from .nodoCircular import Nodo
from .peliculas import Pelicula
from colorama import Fore as fo
import xml.etree.ElementTree as ET
import os

class listaDobleCircular:
    def __init__(self):
        self.cabeza = None

    def add(self, dato):
        nuevo_nodo = Nodo(dato)

        if self.cabeza is None:
            nuevo_nodo.siguiente = nuevo_nodo
            nuevo_nodo.anterior = nuevo_nodo
            self.cabeza = nuevo_nodo
        else:
            ultimo = self.cabeza.anterior

            nuevo_nodo.siguiente = self.cabeza
            nuevo_nodo.anterior = ultimo

            self.cabeza.anterior = nuevo_nodo
            ultimo.siguiente = nuevo_nodo

    def modify(self, dato_nuevo, index):
        actual = self.cabeza
        indice = 0

        while True:
            if indice == index:
                actual.dato = dato_nuevo
                return
            actual = actual.siguiente
            indice += 1
            if actual == self.cabeza:
                break

    def delete(self, dato):
        actual = self.cabeza

        while True:
            if actual.dato == dato:
                if actual.anterior:
                    actual.anterior.siguiente = actual.siguiente
                if actual.siguiente:
                    actual.siguiente.anterior = actual.anterior
                if actual == self.cabeza:
                    self.cabeza = actual.siguiente
                return
            actual = actual.siguiente
            if actual == self.cabeza:
                break

    def search(self, titulo):
        actual = self.cabeza
        while actual:
            if actual.dato.titulo == titulo:
                return actual.dato
            actual = actual.siguiente
        return None

    def show_categorias(self):
        script_dir = os.path.dirname(__file__)

        # Build the path to the XML file by joining the script's directory with the filename
        xml_file_path = os.path.join(script_dir, 'peliculas.xml')

        # Use the path to parse the XML file
        tree = ET.parse(xml_file_path)
        root = tree.getroot()

        print(fo.WHITE + """
        =========== CATEGORIAS ===========""")
        for i, categoria in enumerate(root.findall('categoria')):
            print(fo.WHITE + "                " + f"{i+1}. {categoria.find('nombre').text}")

    def show_peliculas(self, categoria):
        script_dir = os.path.dirname(__file__)

        # Build the path to the XML file by joining the script's directory with the filename
        xml_file_path = os.path.join(script_dir, 'peliculas.xml')

        # Use the path to parse the XML file
        tree = ET.parse(xml_file_path)
        root = tree.getroot()

        categorias = list(root.findall('categoria'))

        # Verifica que no esté fuera de rango
        if categoria < 1 or categoria > len(categorias):
            print(fo.RED + "Categoria no valida")
            return
        
        # Si pasa el test anterior se resta 1 para el indice
        categoria = categorias[categoria-1]
        print(fo.WHITE + f"        =========== {categoria.find('nombre').text} ===========""")
        for indice, pelicula in enumerate(categoria.find('peliculas').findall('pelicula')):
            print(fo.WHITE + "                " + f"{indice + 1}. {pelicula.find('titulo').text}")

    def Imprimir_LDC(self):
        if self.cabeza is None:
            print("La lista esta vacía")
        
        else:
            nodo_actual = self.cabeza
            while True:
                nodo_actual.dato.imprimir()
                nodo_actual = nodo_actual.siguiente

                if nodo_actual == self.cabeza:
                    break

    def CargarXML_LDC(self, operacion):
        script_dir = os.path.dirname(__file__)

        # Build the path to the XML file by joining the script's directory with the filename
        xml_file_path = os.path.join(script_dir, 'peliculas.xml')

        # Use the path to parse the XML file
        tree = ET.parse(xml_file_path)
        root = tree.getroot()

        for category in root.findall('categoria'):
            categoria = category.find('nombre').text
            for indice, movie in enumerate(category.find('peliculas').findall('pelicula')):
                titulo = movie.find('titulo').text
                director = movie.find('director').text
                anio = movie.find('anio').text
                fecha = movie.find('fecha').text
                hora = movie.find('hora').text
                imagen = movie.find('imagen').text
                precio = movie.find('precio').text

                pelicula = Pelicula(categoria, titulo, director, anio, fecha, hora, imagen, precio)

                if operacion == 1:
                    self.add(pelicula)
                elif operacion == 2:
                    self.modify(pelicula, indice)
                elif operacion == 3:
                    self.delete(pelicula)
                

    def editarXML_LDC(self, tmp_titulo, new_fecha, new_hora, new_precio):
        script_dir = os.path.dirname(__file__)

        # Build the path to the XML file by joining the script's directory with the filename
        xml_file_path = os.path.join(script_dir, 'peliculas.xml')

        # Use the path to parse the XML file
        tree = ET.parse(xml_file_path)
        root = tree.getroot()

        for category in root.findall('categoria'):
            for movie in category.find('peliculas').findall('pelicula'):
                if movie.find('titulo').text == tmp_titulo:
                    fecha = movie.find('fecha')
                    fecha.text = new_fecha
                    hora = movie.find('hora')
                    hora.text = new_hora
                    precio = movie.find('precio')
                    precio.text = new_precio
                    break
        
        tree.write(xml_file_path)

        self.cabeza = None  # Clear the list
        self.CargarXML_LDC(1)

    def eliminarXML_LDC(self, tmp_titulo):
        script_dir = os.path.dirname(__file__)

        # Build the path to the XML file by joining the script's directory with the filename
        xml_file_path = os.path.join(script_dir, 'peliculas.xml')

        # Use the path to parse the XML file
        tree = ET.parse(xml_file_path)
        root = tree.getroot()

        for category in root.findall('categoria'):
            for movie in category.find('peliculas').findall('pelicula'):
                if movie.find('titulo').text == tmp_titulo:
                    category.find('peliculas').remove(movie)
                    break

        tree.write(xml_file_path)

        self.CargarXML_LDC(1)