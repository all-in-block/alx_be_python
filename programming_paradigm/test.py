class Book():
    def __init__(self, title,author):
        self.title = title
        self.author = author
        self.___is_checked_out = False
    def booktitle(self):
        return self.title
    def bookauthor(self):
        return self.author
    def is_checked_out(self):
        self.___is_checked_out = True
    def is_avalaible(self):
        return self.___is_checked_out
class Library():
    def __init__(self):
        self.___books: Book = []
    def add_book(self,book):
        self.___books.append(book)
    def check_out_book(self,title):
        for book in self.___booksBook:
            if title == book.bookauthor():
                print(f"the {title} by {self.__books[i].bookauthor()} title exist")
            else:
                print(f"the {title} title dont exist")
    


    def return_book(title):
    def list_available_books():
    




        

