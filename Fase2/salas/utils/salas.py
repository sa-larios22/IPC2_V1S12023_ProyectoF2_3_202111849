from colorama import Fore as fo

class Sala:
    def __init__(self, numero, asientos):
        self.numero = numero
        self.asientos = asientos

    def imprimir(self):
        print(fo.CYAN + "Número de Sala: " + fo.WHITE + self.numero +
              fo. CYAN + " Asientos: " + fo.WHITE + self.asientos)