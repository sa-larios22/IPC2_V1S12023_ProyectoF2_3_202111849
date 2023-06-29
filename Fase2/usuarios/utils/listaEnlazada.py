from .nodo import Nodo
from .usuarios import Usuario
import xml.etree.ElementTree as ET
import os

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None
        default_user = Usuario("administrador", "Sergio", "Larios", "202111849", "1", "1")
        self.add(default_user)

    def add(self, dato):
        
        nuevo = Nodo(dato)

        if self.cabeza is None:
            self.cabeza = nuevo
        else:
            actual = self.cabeza
            while actual.siguiente is not None:
                actual = actual.siguiente
            actual.siguiente = nuevo
    
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
            return

        actual = self.cabeza
        while actual.siguiente is not None:
            if actual.siguiente.dato == dato:
                break
            actual = actual.siguiente

        if actual.siguiente is None:
            return

        actual.siguiente = actual.siguiente.siguiente

    def search(self, correo, contrasena):
        actual = self.cabeza
        while actual:
            if actual.dato.correo == correo and actual.dato.contrasena == contrasena:
                return actual.dato
            actual = actual.siguiente
        return None

    def Imprimir(self):
        actual = self.cabeza
        actual.dato.imprimir()
        while actual.siguiente is not None:
            actual = actual.siguiente
            actual.dato.imprimir()

    def CargarXML(self, operacion):
        # Get the directory that this script is in
        script_dir = os.path.dirname(__file__)

        # Build the path to the XML file by joining the script's directory with the filename
        xml_file_path = os.path.join(script_dir, 'usuarios.xml')

        # Use the path to parse the XML file
        tree = ET.parse(xml_file_path)
        root = tree.getroot()

        for indice, users in enumerate(root.findall('usuario')):
            rol = users.find('rol').text
            nombre = users.find('nombre').text
            apellido = users.find('apellido').text
            telefono = users.find('telefono').text
            correo = users.find('correo').text
            contrasena = users.find('contrasena').text

            objeto = Usuario(rol, nombre, apellido, telefono, correo, contrasena)

            if operacion == 1: # agregar datos a lista
                self.add(objeto)
            elif operacion == 2:
                self.modify(objeto, indice)
            elif operacion == 3:
                self.delete(objeto)

    def agregarXML(self, rol, nombre, apellido, telefono, correo, contrasena):
        script_dir = os.path.dirname(__file__)
        xml_file_path = os.path.join(script_dir, 'usuarios.xml')
        tree = ET.parse(xml_file_path)
        root = tree.getroot()
        
        new_user = ET.SubElement(root, 'usuario')
        
        ET.SubElement(new_user, 'rol').text = rol
        ET.SubElement(new_user, 'nombre').text = nombre
        ET.SubElement(new_user, 'apellido').text = apellido
        ET.SubElement(new_user, 'telefono').text = telefono
        ET.SubElement(new_user, 'correo').text = correo
        ET.SubElement(new_user, 'contrasena').text = contrasena
        
        self.indent_usuarios(root)
        
        try:
            tree.write(xml_file_path)
        except Exception as e:
            print(e)

    def editarXML(self, new_rol, new_nombre, new_apellido, new_telefono, tmp_correo, new_contrasena):
        # Get the directory that this script is in
        script_dir = os.path.dirname(__file__)

        # Build the path to the XML file by joining the script's directory with the filename
        xml_file_path = os.path.join(script_dir, 'usuarios.xml')

        # Use the path to parse the XML file
        tree = ET.parse(xml_file_path)
        root = tree.getroot()

        for user in root.findall('usuario'):
            if user.find('correo').text == tmp_correo:
                rol = user.find('rol')
                rol.text = new_rol
                nombre = user.find('nombre')
                nombre.text = new_nombre
                apellido = user.find('apellido')
                apellido.text = new_apellido
                telefono = user.find('telefono')
                telefono.text = new_telefono
                contrasena = user.find('contrasena')
                contrasena.text = new_contrasena
                break

        tree.write(xml_file_path)

        self.CargarXML(2)

    def eliminarXML(self, tmp_correo):
        # Get the directory that this script is in
        script_dir = os.path.dirname(__file__)

        # Build the path to the XML file by joining the script's directory with the filename
        xml_file_path = os.path.join(script_dir, 'usuarios.xml')

        # Use the path to parse the XML file
        tree = ET.parse(xml_file_path)
        root = tree.getroot()

        for user in root.findall('usuario'):
            if user.find('correo').text == tmp_correo:
                root.remove(user)
                break

        tree.write(xml_file_path)
        
    def indent_usuarios(self, elem, level=0):
        i = "\n" + level*"  "
        if len(elem):
            if not elem.text or not elem.text.strip():
                elem.text = i + "  "
            if not elem.tail or not elem.tail.strip():
                elem.tail = i
            for elem in elem:
                self.indent_usuarios(elem, level+1)
            if not elem.tail or not elem.tail.strip():
                elem.tail = i
        else:
            if level and (not elem.tail or not elem.tail.strip()):
                elem.tail = i