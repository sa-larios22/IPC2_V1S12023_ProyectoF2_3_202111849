from .nodoCircular import Nodo
from .peliculas import Pelicula
from colorama import Fore as fo
import xml.etree.ElementTree as ET
import os

class listaDobleCircular:
    def __init__(self):
        self.cabeza = None
        
    def __iter__(self):
        node = self.cabeza
        while True:
            yield node
            node = node.siguiente
            if node == self.cabeza:
                break

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

    def empty(self):
        self.cabeza = None

    def get_all_titulos(self):
        if self.cabeza is None:
            print("La lista esta vacía")
            return []

        result = []
        nodo_actual = self.cabeza
        while True:
            pelicula = nodo_actual.dato
            result.append(pelicula.titulo)
            nodo_actual = nodo_actual.siguiente

            if nodo_actual == self.cabeza:
                break

        return result

    def get_all_imagenes(self):
        if self.cabeza is None:
            print("La lista esta vacía")
            return []

        result = []
        nodo_actual = self.cabeza
        while True:
            pelicula = nodo_actual.dato
            result.append(pelicula.imagen)
            nodo_actual = nodo_actual.siguiente

            if nodo_actual == self.cabeza:
                break

        return result

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
                

    def agregarXML_LDC(self, categoria, titulo, director, anio, fecha, hora, imagen, precio):
        script_dir = os.path.dirname(__file__)
        xml_file_path = os.path.join(script_dir, 'peliculas.xml')
        tree = ET.parse(xml_file_path)
        root = tree.getroot()
        
        # Check if categoria already exists
        categoria_element = None
        for cat in root.findall('categoria'):
            nombre = cat.find('nombre')
            if nombre is not None and nombre.text == categoria:
                categoria_element = cat
                break
        
        # If the categoria doesn't exist, create it    
        if categoria_element is None:
            categoria_element = ET.SubElement(root, 'categoria')
            ET.SubElement(categoria_element, 'nombre').text = categoria
            peliculas_element = ET.SubElement(categoria_element, 'peliculas')
        else:
            peliculas_element = categoria_element.find('peliculas')

        new_movie = ET.SubElement(peliculas_element, 'pelicula')
        
        ET.SubElement(new_movie, 'titulo').text = titulo
        ET.SubElement(new_movie, 'director').text = director
        ET.SubElement(new_movie, 'anio').text = anio
        ET.SubElement(new_movie, 'fecha').text = fecha
        ET.SubElement(new_movie, 'hora').text = hora
        ET.SubElement(new_movie, 'imagen').text = imagen
        ET.SubElement(new_movie, 'precio').text = precio
        
        self.indent_movies(root)
        
        try:
            tree.write(xml_file_path)
        except Exception as e:
            print(e)
        

    def editarXML_LDC(self, pelicula):
        script_dir = os.path.dirname(__file__)
        xml_file_path = os.path.join(script_dir, 'peliculas.xml')
        tree = ET.parse(xml_file_path)
        root = tree.getroot()

        old_movie_element = None
        old_categoria_element = None

        # Search for the old movie and its category
        for category in root.findall('categoria'):
            for movie in category.find('peliculas').findall('pelicula'):
                if movie.find('titulo').text == pelicula.titulo:
                    old_movie_element = movie
                    old_categoria_element = category
                    break
            if old_movie_element is not None:
                break
        
        # If the old movie wasn't found, just return
        if old_movie_element is None:
            print("Movie not found")
            return

        # Use the "eliminarXML_LDC" method to remove the old movie
        self.eliminarXML_LDC(pelicula.titulo)

        # Now, call the "agregarXML_LDC" method to add the updated movie in its new category
        self.agregarXML_LDC(pelicula.categoria, pelicula.titulo, pelicula.director, pelicula.anio, pelicula.fecha, pelicula.hora, pelicula.imagen, pelicula.precio)

        self.cabeza = None  # Clear the list

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
        
    def indent_movies(self, elem, level=0):
        i = "\n" + level*"  "
        if len(elem):
            if not elem.text or not elem.text.strip():
                elem.text = i + "  "
            if not elem.tail or not elem.tail.strip():
                elem.tail = i
            for elem in elem:
                self.indent_movies(elem, level+1)
            if not elem.tail or not elem.tail.strip():
                elem.tail = i
        else:
            if level and (not elem.tail or not elem.tail.strip()):
                elem.tail = i