import datetime
import Libraries.library as lib


class Employee:
    def __init__(self, first_name: str, last_name: str, hired_date: datetime.date, birth_date: datetime.date,
                 city: str, street: str, zip_code: int, phone: int, library: lib.Library) -> object:
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
