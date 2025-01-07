from models.irasas import Irasas


class IslaiduIrasas(Irasas):
    def __repr__(self):
        return f"Išlaidos: {self.suma}"