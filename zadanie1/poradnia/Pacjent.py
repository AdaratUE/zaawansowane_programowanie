import poradnia.Osoba as os


class Pacjent(os.Osoba):
    def __init__(self, imie, nazwisko, numer_telefonu, id_pacjenta: str):
        super().__init__(imie, nazwisko, numer_telefonu)
        self.__id_pacjenta = id_pacjenta

    @property
    def id_pacjenta(self):
        return self.__id_pacjenta

    def __str__(self):
        return f"Pacjent {self.imie} {self.nazwisko} " \
               f"o numerze telefonu: {self.numer_telefonu}" \
               f"i id: {self.__id_pacjenta}"
