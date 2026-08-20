class Library:
    def __init__(self):
        self.__books = []

    def add_book(self, book):
        self.__books.append(book)

    def remove_book(self, book):
        if book in self.__books:
            self.__books.remove(book)

    def list_books(self):
        for book in self.__books:
            print(book)


library = Library()

library.add_book("Python Basics")
library.add_book("OOP in Python")
library.add_book("Learn Coding")

library.remove_book("OOP in Python")

library.list_books()