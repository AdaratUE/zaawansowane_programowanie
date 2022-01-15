import datetime

import poradnia.Dietetyk as Dietetyk
import poradnia.Pacjent as Pacjent


class Zamowienie():
    def __init__(self, dietetyk: Dietetyk.Dietetyk, pacjent: Pacjent.Pacjent,
                 diety: list(), data_wydania: datetime):
        self.__dietetyk = dietetyk
        self.__pacjent = pacjent
        self.__diety = diety
        self.__data_wydania = data_wydania

    @property
    def dietetyk(self):
        return self.__dietetyk

    @dietetyk.setter
    def dietetyk(self, value: object):
        self.__dietetyk = value

    @property
    def pacjent(self):
        return self.__pacjent

    @pacjent.setter
    def pacjent(self, value: object):
        self.__pacjent = value

    @property
    def diety(self):
        return self.__diety

    @diety.setter
    def diety(self, value: list()):
        self.__diety = value

    @property
    def data_wydania(self):
        return self.__data_wydania

    @data_wydania.setter
    def data_wydania(self, value: datetime):
        self.__data_wydania = value

    def licz_cene(self) -> float:
        suma = 0
        for x in self.__diety:
            suma += x.koszt_diety
        return round(suma, 2)

    def licz_kalorii(self) -> int:
        suma = 0
        for x in self.__diety:
            suma += x.kalorie
        return suma

    def __str__(self):
        return f"Zamowienie dla pacjenta {self.__pacjent.imie}, " \
               f"wydana: {self.__data_wydania} kosztuje {self.licz_cene()}" \
               f" i składa się z {self.licz_kalorii()} kalorii"
