class Odcinek:
    def __init__(self, lok_pocz: str, lok_koncowa: str, odleglosc: int, identyfikator: str, wartosc: int):
        self.__lok_pocz = lok_pocz
        self.__lok_koncowa = lok_koncowa
        self.__odleglosc = odleglosc
        self.__identyfikator = identyfikator
        self.__wartosc = wartosc

    @property
    def odleglosc(self):
        return self.__odleglosc

    def __str__(self):
        return f"Od {self.__lok_pocz} do {self.__lok_koncowa}"