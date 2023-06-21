from colorama import Fore as fo

class Pelicula:
    def __init__(self, categoria, titulo, director, anio, fecha, hora):
        self.categoria = categoria
        self.titulo = titulo
        self.director = director
        self.anio = anio
        self.fecha = fecha
        self.hora = hora

    def imprimir(self):
        print(fo.CYAN + "Categoria: " + fo.WHITE + self.categoria +
              fo.CYAN + " Titulo: " + fo.WHITE + self.titulo +
              fo.CYAN + " Director: " + fo.WHITE + self.director +
              fo.CYAN + " Año: " + fo.WHITE + self.anio +
              fo.CYAN + " Fecha: " + fo.WHITE + self.fecha +
              fo.CYAN + " Hora: " + fo.WHITE + self.hora)