from colorama import Fore as fo

class Usuario:
    def __init__(self, rol, nombre, apellido, telefono, correo, contrasena):
        self.rol = rol
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.correo = correo
        self.contrasena = contrasena

    def imprimir(self):
        print(fo.CYAN + "Rol: " + fo.WHITE + self.rol +
              fo.CYAN + ", Nombre: " + fo.WHITE + self.nombre,
              fo.CYAN + ", Apellido: " + fo.WHITE + self.apellido +
              fo.CYAN + ", Teléfono: " + fo.WHITE + self.telefono +
              fo.CYAN + ", Correo: " + fo.WHITE + self.correo +
              fo.CYAN + ", Contraseña: " + fo.WHITE + self.contrasena
              + fo.RESET)