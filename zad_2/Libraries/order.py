import datetime
import Libraries.employee as empl
import Libraries.student as stud
import Libraries.book as book


class Order:
    def __init__(self, employee: empl.Employee, student: stud.Student,
                 books: book.Book, order_date: datetime.date) -> object:
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date

    def __str__(self):
        return f'Książka pt {self.books.title} została wydana przez {self.employee.first_name} ' \
               f'{self.employee.last_name} dnia {self.order_date} studentowi {self.student.student_name} ' \
               f'{self.student.student_surname}'
