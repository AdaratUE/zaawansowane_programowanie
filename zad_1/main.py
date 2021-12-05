from firmy.firma_spozywcza import FirmaSpozywcza
from firmy.firma_transportowa import FirmaTransportowa
from firmy.pojazd import Pojazd
from kursy.kurs import Kurs
from kursy.odcinek import Odcinek


pojazd1 = Pojazd("BMW", "1993", 5081, "35s", "BMwds132")
firmaT1 = FirmaTransportowa("Ja jade", [pojazd1], 33, "Białystok", 503555999)
firmaS1 = FirmaSpozywcza("Ogryzek", "Katowice", 666999555, "2001", "BS3")
odcinek1 = Odcinek("Gniezno", "Wielkowies", 304, "Ale2", 675)
odcinek2 = Odcinek("Wielkowies", "Krakow", 408, "Ale4", 888)
kurs1 = Kurs([odcinek2.odleglosc, odcinek1.odleglosc], firmaS1, firmaT1, pojazd1, "20-1-2021")

print(kurs1)