import datetime

import poradnia.Dieta as Dieta
import poradnia.Dietetyk as Dietetyk
import poradnia.Pacjent as Pac
import poradnia.Zamowienie as Zam


dieta1 = Dieta.Dieta("Czajkowskiego", 72.43, "3de", 3222)
dieta2 = Dieta.Dieta("Dąbrowskiego", 55.56, "4es", 2222)
dietetyk1 = Dietetyk.Dietetyk("Jan", "Kowalski", 123123123, "sw132")
pacjent1 = Pac.Pacjent("Ewa", "Wysocka", 666688886, "as32132")
zamowienie1 = Zam.Zamowienie(dietetyk1, pacjent1, [dieta1, dieta2],
                             datetime.datetime(2021, 2, 11))
print(zamowienie1)


