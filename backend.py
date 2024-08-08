import json

class Book:
    def __init__(self, id, name, year, author):
        self.id = id
        self.name = name
        self.author = author
        self.year = year

class Library:
    def __init__(self):
        self.database = json.load(open('./database.json'))
    
    def add_book(self):
        pass

    def remove_book(self):
        pass

    def search_book(self):
        pass

    def get_all_books(self):
        pass

    def get_book_names(self):
        result = [
            self.database[book]["name"] 
            for book in self.database.keys()
        ]
        return result


library = Library()
print(library.get_book_names())
