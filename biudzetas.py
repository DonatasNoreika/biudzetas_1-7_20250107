from models.pajamu_irasas import PajamuIrasas
from models.islaidu_irasas import IslaiduIrasas


class Biudzetas:
    def __init__(self):
        self.zurnalas = []

    def prideti_pajamas(self):
        suma = float(input("Suma: "))
        irasas = PajamuIrasas(suma)
        self.zurnalas.append(irasas)

    def prideti_islaidas(self):
        suma = float(input("Suma: "))
        irasas = IslaiduIrasas(suma)
        self.zurnalas.append(irasas)

    def gauti_balansa(self):
        balansas = 0
        for irasas in self.zurnalas:
            if type(irasas) is PajamuIrasas:
                balansas += irasas.suma
            else:
                balansas -= irasas.suma
        return balansas
