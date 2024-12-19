from datetime import date


class Library:
    def __init__(self):
        self.catalog = []

    def add(self, book):
        self.catalog.append(book)

    def lookup_author(self,author):
        result = []
        for book in self.catalog:
            if book.author == author:
                result.append(book)



class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        if year > date.today().year:
            raise
        self.year = year

