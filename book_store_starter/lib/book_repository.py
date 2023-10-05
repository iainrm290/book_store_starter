from lib.book import Book

# Class design

# class BookRepository


# __init__ method
# This is initialised with a database connection
class BookRepository:
    def __init__(self, connection):
        self.connection = connection


# all method
# This retrieves a list of book objects
# Returns a formatted list of objects
    def all(self):
        rows = self.connection.execute('SELECT * from books')
        books = []
        for row in rows:
            item = Book(row["id"], row["title"], row["author_name"])
            books.append(item)
        return books