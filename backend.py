import json

class Book:
    def __init__(self, id, name, year, author):
        self.id = id
        self.name = name
        self.year = year
        self.author = author

    def get_key_value(self):
        key_value = {
            "name":self.name,
            "year":self.year,
            "author":self.author
        }
        return key_value

class Library:
    def __init__(self):
        file = open("./database.json", "r")
        self.database: dict = json.load(file)


    def add_book(self, id, name, year, author):
        if id in self.database.keys():
            raise ValueError("id already exists")
        else:
            newBook = Book(id, name, year, author)
            self.database[id] = newBook.get_key_value()
            file = open("./database.json", "w")
            json.dump(
                self.database, 
                file,
                indent=4
            )


    def remove_book(self):
        pass

    def search_book(self):
        pass

    def get_all_books(self):
        pass

    def get_book_names(self):
        result = [
            self.database[id]["name"] 
            for id in self.database.keys()
        ]
        return result


library = Library()
library.add_book(
    "id0004", 
    "Harry Potter 4",
    2009,
    "J.K. Rolling"
)
library.add_book(
    "id0005", 
    "Harry Potter 4",
    2009,
    "J.K. Rolling"
)
library.add_book(
    "id0006", 
    "Harry Potter 4",
    2009,
    "J.K. Rolling"
)
library.add_book(
    "id0001", 
    "Harry Potter 4",
    2009,
    "J.K. Rolling"
)


