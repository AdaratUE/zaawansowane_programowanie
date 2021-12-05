from firmy.firma import Firma


class FirmaSpozywcza(Firma):
    def __init__(self, nazwa, lokalizacja: str, numer_telefonu: int, rok_zalozenia: str, kategoria: str):
        super().__init__(nazwa, lokalizacja, numer_telefonu)
        self.__lokalizacja = lokalizacja
        self.__numer_telefonu = numer_telefonu
        self.__rok_zalozenia = rok_zalozenia
        self.__kategoria = kategoria


    def __str__(self):
        return f"Firma {self.__nazwa} kategorii {self.__kategoria} znajduje się w {self.__lokalizacja}"
