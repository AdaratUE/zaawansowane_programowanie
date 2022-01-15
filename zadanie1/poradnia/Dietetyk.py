import poradnia.Osoba as os


class Dietetyk(os.Osoba):
    def __init__(self, imie, nazwisko, numer_telefonu, id_pracownika: str):
        super().__init__(imie, nazwisko, numer_telefonu)
        self.__id_pracownika = id_pracownika

    @property
    def id_pracownika(self):
        return self.__id_pracownika

    def __str__(self):
        return f"Dietetyk {self.imie} {self.nazwisko} o " \
               f"numerze telefonu: {self.numer_telefonu}" \
               f"o id pracownika: {self.__id_pracownika}"
