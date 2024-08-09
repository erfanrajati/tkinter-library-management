import json

class Book:
    def __init__(self, name, year, author):
        self.id = self.generate_id()
        self.name = name
        self.year = year
        self.author = author

    # initializer for testing
    # def __init__(self):
    #     # self.id = self.generate_id()
    #     self.name = "name"
    #     self.year = "year"
    #     self.author = "author"

    def get_key_value(self):
        key_value = {
            "name":self.name,
            "year":self.year,
            "author":self.author
        }
        return key_value

    def generate_id(self):
        file = open("./database.json", "r")
        db: dict = json.load(file)
        id_list = [int(id.split('-')[1]) for id in db.keys()]
        id_list.sort()
        for i in range(id_list[0], id_list[-1]+2):
            if i not in id_list:
                new_id = i
                break
        return "id-" + str(10000 + new_id)[1:]
        # print("id-" + str(10000 + new_id)[1:])

class Library:
    def __init__(self):
        file = open("./database.json", "r")
        self.database: dict = json.load(file)

    def get_book_names(self):
        result = [
            self.database[id]["name"] 
            for id in self.database.keys()
        ]
        return result

    def add_book(self, name, year, author):
        # if id in self.database.keys():
        #     raise ValueError("id already exists")
        # else:
        newBook = Book(name, year, author)
        self.database[newBook.id] = newBook.get_key_value()
        file = open("./database.json", "w")
        json.dump(self.database, file, indent=4)

    def remove_book(self):
        pass

    def search_book(self):
        pass

    def get_all_books(self):
        pass





