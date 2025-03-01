class Author:
    def __init__(self, author_name):
        self.author_name = author_name
    
    def get_author(self):
        return self.author_name

class Book:
    def __init__(self, book_name, author):
        self.book_name = book_name
        self.author = author  
        
    def display(self):
        print("Author:", self.author.get_author())
        print("Book Name:", self.book_name)

a = Author("NKV")
b = Book("Agni", a)

b.display()
