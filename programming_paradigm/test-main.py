class Book():
    def __init__(self,title,author):
        self.title = title
        self.author = author
        self.books = []

    def __str__(self):
        return f"book with {self.title} by {self.author}"
    
    def addbook(self,book):
        self.books.append(book)
    def booksadded(self):
        return self.books


def main():
    title = input("enter the title ")
    author = input("enter the author ")
    newbook1 = Book(title,author)
    newbook2 = Book(title,author)
    newbook3 = Book(title,author)
    booktoadd1 = newbook1.addbook(newbook1)
    booktoadd2 = newbook2.addbook(newbook2)
    booktoadd3 = newbook3.addbook(newbook3)
    print("---------")
    print()
main()

