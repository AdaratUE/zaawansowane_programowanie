from firmy.firma import Firma


class FirmaTransportowa(Firma):
    def __init__(self, nazwa, lista_pojazdow: list(), ilu_pracownikow: int, lokalizacja, numer_telefonu):
        super().__init__(nazwa, lokalizacja, numer_telefonu)
        self.__lista_pojazdow = lista_pojazdow
        self.__ilu_pracownikow = ilu_pracownikow
        self.__numer_telefonu = numer_telefonu



    @property
    def lista_pojazdow(self):
        return self.__lista_pojazdow

    @property
    def ilu_pracownikow(self):
        return self.__ilu_pracownikow

    @property
    def marka(self):
        return self.__lokalizacja

    @property
    def __str__(self):
        return f"Firma {self.__nazwa} posiada {len(self.__lista_pojazdow)}"
