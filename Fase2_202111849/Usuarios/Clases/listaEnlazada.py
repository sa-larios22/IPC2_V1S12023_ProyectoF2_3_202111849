from Usuarios.Clases.nodo import Nodo
from Usuarios.Clases.usuarios import Usuario
import xml.etree.ElementTree as ET

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None
        default_user = Usuario("administrador", "Sergio", "Larios", "202111849", "1", "1")
        self.add(default_user)

    def __iter__(self):
        return iter(self.loop())
    
    def loop(self):
        actual = self.cabeza
       
        while actual:
            yield actual.dato
            actual = actual.siguiente

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
        
        tree = ET.parse('Usuarios\\Clases\\usuarios.xml')
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

    def editarXML(self, new_rol, new_nombre, new_apellido, new_telefono, tmp_correo, new_contrasena):
        tree = ET.parse('usuarios.xml')
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

        tree.write('usuarios.xml')

        self.CargarXML(2)

    def eliminarXML(self, tmp_correo):
        tree = ET.parse('usuarios.xml')
        root = tree.getroot()

        for user in root.findall('usuario'):
            if user.find('correo').text == tmp_correo:
                root.remove(user)
                break

        tree.write('usuarios.xml')

        self.CargarXML(3)