import datetime
import Libraries.library as lib
import Libraries.book as book
import Libraries.employee as empl
import Libraries.order as ord
import Libraries.student as stud


bibl1 = lib.Library('Katowice', 'Mariacka 3', 40001, '06-18', 303212132)
bibl2 = lib.Library('Czechowice-Dziedzice', 'Jakas 3', 43502, '08-18', 333999666)

stud1 = stud.Student('Jan', 'Kowalski', 34052)
stud2 = stud.Student('Rafał', 'Jakis', 53022)
stud3 = stud.Student('Ewa', 'Kaczka', 11051)

book1 = book.Book(bibl1, 'Ksiazka 1', datetime.date(2020, 5, 17), 'Jan', 'Kowalski', 303)
book2 = book.Book(bibl2, 'Ksiazka 2', datetime.date(2000, 4, 2), 'Jan', 'Matejko', 211)
book3 = book.Book(bibl2, 'Ksiazka 3', datetime.date(1321, 4, 2), 'Ola', 'Jakas', 921)
book4 = book.Book(bibl2, 'Ksiazka 4', datetime.date(1995, 4, 2), 'Adam', 'Kłos', 244)
book5 = book.Book(bibl2, 'Ksiazka 5', datetime.date(2010, 4, 2), 'Piotr', 'Zacny', 55)

empl1 = empl.Employee('Jeży', 'Rajski', datetime.date(2019, 3, 11), datetime.date(2000, 2, 2),
                      'Kraków', 'Jutrzenki 2', 40321, 1231321230, bibl2)
empl2 = empl.Employee('Katarzyna', 'Rydz', datetime.date(2018, 3, 11), datetime.date(1993, 1, 1),
                      'Katowice', 'Jutrzenki 2', 40001, 777777777, bibl1)
empl3 = empl.Employee('Paweł', 'Piotr', datetime.date(2017, 3, 11), datetime.date(1960, 1, 3),
                      'Kraków', 'Jutrzenki 2', 42131, 111111111, bibl1)

ord1 = ord.Order(empl1, stud3, book5, datetime.date(2021, 11, 22))
ord2 = ord.Order(empl2, stud1, book2, datetime.date(2021, 10, 11))

print(ord1)
print(ord2)
