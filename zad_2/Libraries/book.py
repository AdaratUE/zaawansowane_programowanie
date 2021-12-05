import datetime
import Libraries.library as lib


class Book:
    def __init__(self, library: lib.Library, title: str, publication_date: datetime.date, author_name: str,
                 author_surname: str, number_of_pages: int) -> object:
        self.library = library
        self.title = title
        self.publication_date = publication_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_of_pages = number_of_pages

    def __str__(self):
        return f'Książka pod tytułem: {self.title}  wydana: {self.publication_date} znajduje się w biblotece w' \
               f' mieście: {self.library.city}'

