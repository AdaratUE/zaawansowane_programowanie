class Dieta:
    def __init__(self, nazwa_diety: str, koszt_diety: float,
                 kategoria_diety: str, kalorie: int):
        self.__nazwa_diety = nazwa_diety
        self.__koszt_diety = koszt_diety
        self.__kategoria_diety = kategoria_diety
        self.__kalorie = kalorie

    @property
    def nazwa_diety(self):
        return self.__nazwa_diety

    @property
    def koszt_diety(self):
        return self.__koszt_diety

    @property
    def kategoria_diety(self):
        return self.__kategoria_diety

    @property
    def kalorie(self):
        return self.__kalorie

    def __str__(self):
        return f"Dieta nazywa się: {self.__nazwa_diety} " \
               f"i ma {self.__kalorie_} kalorii, kosztuje " \
               f"{self.__koszt_diety}, a jej kategoria " \
               f"to {self.__kategoria_diety}"
