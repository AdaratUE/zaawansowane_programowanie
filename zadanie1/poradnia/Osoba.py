class Osoba:
    def __init__(self, imie: str, nazwisko: str, numer_telefonu: int):
        self.__imie = imie
        self.__nazwisko = nazwisko
        self.__numer_telefonu = numer_telefonu

    @property
    def imie(self):
        return self.__imie

    @property
    def nazwisko(self):
        return self.__nazwisko

    @property
    def numer_telefonu(self):
        return self.__numer_telefonu

    def __str__(self):
        return f"Osoba {self.imie} {self.nazwisko} " \
               f"o numerze telefonu: {self.numer_telefonu}"
