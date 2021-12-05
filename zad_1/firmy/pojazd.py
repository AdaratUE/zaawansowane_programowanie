class Pojazd:
    def __init__(self, marka: str, rok_prod: str, przejechane: int, model: str, identyfikator: str):
        self.__marka = marka
        self.__rok_prod = rok_prod
        self.__przejechane = przejechane
        self.__model = model
        self.__identyfikator = identyfikator

    @property
    def marka(self):
        return self.__marka

    @property
    def rok_prod(self):
        return self.__rok_prod

    @property
    def przejechane(self):
        return self.__przejechane

    @property
    def model(self):
        return self.__model

    @property
    def identyfikator(self):
        return self.__identyfikator

    def __str__(self):
        return f"Marka: {self.__marka}, identyfikator: {self.__identyfikator}"