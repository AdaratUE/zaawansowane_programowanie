import firmy.pojazd as Pojazd
from firmy.firma_spozywcza import FirmaSpozywcza
from firmy.firma_transportowa import FirmaTransportowa

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
