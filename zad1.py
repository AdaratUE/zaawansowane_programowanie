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

class Firma:
    def __init__(self, nazwa: str):
        self.nazwa = nazwa

class FirmaTransportowa(Firma):
    def __init__(self, nazwa, lista_pojazdow: list(), ilu_pracownikow: int, lokalizacja: str, numer_telefonu: int):
        super().__init__(nazwa)
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


class FirmaSpozywcza(Firma):
    def __init__(self, nazwa, lokalizacja: str, numer_telefonu: int, rok_zalozenia: str, kategoria: str):
        super().__init__(nazwa)
        self.__lokalizacja = lokalizacja
        self.__numer_telefonu = numer_telefonu
        self.__rok_zalozenia = rok_zalozenia
        self.__kategoria = kategoria


    def __str__(self):
        return f"Firma {self.__nazwa} kategorii {self.__kategoria} znajduje się w {self.__lokalizacja}"


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


class Kurs:
    def __init__(self, odcinki: list(), firma_spozywcza: FirmaSpozywcza, firma_transportowa: FirmaTransportowa,
                 pojazd: Pojazd, data_kursu: str):
        self.__odcinki = odcinki
        self.__firma_spozywcza = firma_spozywcza
        self.__firma_transportowa = firma_transportowa
        self.__pojazd = pojazd
        self.__data_kursu = data_kursu

    @property
    def odcinki(self):
        return self.__odcinki

    @odcinki.setter
    def odcinki(self, value: list()):
        self.__odcinki = value

    @property
    def firma_spozywcza(self):
        return self.__firma_spozywcza

    @firma_spozywcza.setter
    def firma_spozywcza(self, value: FirmaSpozywcza):
        self.__firma_spozywcza = value

    @property
    def firma_transportowa(self):
        return self.__firma_transportowa

    @firma_transportowa.setter
    def firma_transportowa(self, value: FirmaTransportowa):
        self.__firma_transportowa = value

    @property
    def pojazd(self):
        return self.__pojazd

    @pojazd.setter
    def pojazd(self, value: Pojazd):
        self.__pojazd = value

    @property
    def data_kursu(self):
        return self.__data_kursu

    @data_kursu.setter
    def data_kursu(self, value: str):
        self.__data_kursu = value

    def licz(self) -> int:
        return sum(self.__odcinki)

    def wyswietl_marke(self) -> str:
        return self.__pojazd.marka

    def __str__(self):
        return f"Pojazd {self.wyswietl_marke()} pokonał odcinki o sumie {self.licz()} , został on wysłany przez " \
               f"firmę {self.__firma_transportowa.nazwa} na zlecenie {self.__firma_spozywcza.nazwa}"


pojazd1 = Pojazd("BMW", "1993", 5081, "35s", "BMwds132")
firmaT1 = FirmaTransportowa("Ja jade", [pojazd1], 33, "Białystok", 503555999)
firmaS1 = FirmaSpozywcza("Ogryzek", "Katowice", 666999555, "2001", "BS3")
odcinek1 = Odcinek("Gniezno", "Wielkowies", 304, "Ale2", 675)
odcinek2 = Odcinek("Wielkowies", "Krakow", 408, "Ale4", 888)
kurs1 = Kurs([odcinek2.odleglosc, odcinek1.odleglosc], firmaS1, firmaT1, pojazd1, "20-1-2021")

print(kurs1)
