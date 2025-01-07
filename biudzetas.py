from models.pajamu_irasas import PajamuIrasas
from models.islaidu_irasas import IslaiduIrasas
import pickle

class Biudzetas:
    def __init__(self):
        self.zurnalas = self.gauti_zurnala()

    def gauti_zurnala(self):
        try:
            with open("biudzetas.pkl", 'rb') as file:
                zurnalas = pickle.load(file)
        except FileNotFoundError:
            zurnalas = []
        return zurnalas

    def irasyti_zurnala(self):
        with open("biudzetas.pkl", 'wb') as file:
            pickle.dump(self.zurnalas, file)

    def prideti_pajamas(self):
        suma = float(input("Suma: "))
        irasas = PajamuIrasas(suma)
        self.zurnalas.append(irasas)
        self.irasyti_zurnala()

    def prideti_islaidas(self):
        suma = float(input("Suma: "))
        irasas = IslaiduIrasas(suma)
        self.zurnalas.append(irasas)
        self.irasyti_zurnala()

    def gauti_balansa(self):
        balansas = 0
        for irasas in self.zurnalas:
            if type(irasas) is PajamuIrasas:
                balansas += irasas.suma
            else:
                balansas -= irasas.suma
        return balansas
