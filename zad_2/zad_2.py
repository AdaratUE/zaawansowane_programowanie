import datetime
import libraries.l



class Employee:
    def __init__(self, first_name: str, last_name: str, hired_date: datetime.date, birth_date: datetime.date,
                 city: str, street: str, zip_code: int, phone: int, library: Library) -> object:
        self.first_name = first_name
        self.last_name = last_name
        self.hired_date = hired_date
        self.birth_date = birth_date
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.phone = phone
        self.library = library

    def __str__(self):
        return f'{self.fist.name} {self.last_name} mieszka w {self.city}'


class Book:
    def __init__(self, library: Library, title: str, publication_date: datetime.date, author_name: str, author_surname: str,
                 number_of_pages: int) -> object:
        self.library = library
        self.title = title
        self.publication_date = publication_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_of_pages = number_of_pages

    def __str__(self):
        return f'Książka pod tytułem: {self.title}  wydana: {self.publication_date} znajduje się w biblotece w' \
               f' mieście: {self.library.city}'


class Student:
    def __init__(self, student_name: str, student_surname: str, student_id: int) -> object:
        self.student_name = student_name
        self.student_surname = student_surname
        self.student_id = student_id

    def __str__(self):
        return f'{self.student_surname} {self.student_name} o numerze {self.student_id}'


class Order:
    def __init__(self, employee: Employee, student: Student, books: Book, order_date: datetime.date) -> object:
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date

    def __str__(self):
        return f'Książka pt {self.books.title} została wydana przez {self.employee.first_name} {self.employee.last_name} ' \
               f'dnia {self.order_date} studentowi {self.student.student_name} {self.student.student_surname}'


bibl1 = Library('Katowice', 'Mariacka 3', 40001, '06-18', 303212132)
bibl2 = Library('Czechowice-Dziedzice', 'Jakas 3', 43502, '08-18', 333999666)

stud1 = Student('Jan', 'Kowalski', 34052)
stud2 = Student('Rafał', 'Jakis', 53022)
stud3 = Student('Ewa', 'Kaczka', 11051)

book1 = Book(bibl1, 'Ksiazka 1', datetime.date(2020, 5, 17), 'Jan', 'Kowalski', 303)
book2 = Book(bibl2, 'Ksiazka 2', datetime.date(2000, 4, 2), 'Jan', 'Matejko', 211)
book3 = Book(bibl2, 'Ksiazka 3', datetime.date(1321, 4, 2), 'Ola', 'Jakas', 921)
book4 = Book(bibl2, 'Ksiazka 4', datetime.date(1995, 4, 2), 'Adam', 'Kłos', 244)
book5 = Book(bibl2, 'Ksiazka 5', datetime.date(2010, 4, 2), 'Piotr', 'Zacny', 55)

empl1 = Employee('Jeży', 'Rajski', datetime.date(2019, 3, 11), datetime.date(2000, 2, 2), 'Kraków', 'Jutrzenki 2', 40321, 1231321230, bibl2)
empl2 = Employee('Katarzyna', 'Rydz', datetime.date(2018, 3, 11), datetime.date(1993, 1, 1), 'Katowice', 'Jutrzenki 2', 40001, 777777777, bibl1)
empl3 = Employee('Paweł', 'Piotr', datetime.date(2017, 3, 11), datetime.date(1960, 1, 3), 'Kraków', 'Jutrzenki 2', 42131, 111111111, bibl1)

ord1 = Order(empl1, stud3, book5, datetime.date(2021, 11, 22))
ord2 = Order(empl2, stud1, book2, datetime.date(2021, 10, 11))

print(ord1)
print(ord2)



