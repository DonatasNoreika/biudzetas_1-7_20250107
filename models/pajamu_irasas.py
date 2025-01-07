from models.irasas import Irasas


class PajamuIrasas(Irasas):
    def __repr__(self):
        return f"Pajamos: {self.suma}"