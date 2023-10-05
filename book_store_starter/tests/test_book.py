from lib.book import Book
# I want to test that Book constructs with id, title, and author name
def test_book_constructs():
    book = Book(1, "White Noise", "Don Delillo")
    assert book.id == 1
    assert book.title == "White Noise"
    assert book.author_name == "Don Delillo"

# I want to test that book details are formatted in a readable way for the user
def test_book_formatting():
    book = Book(1, "White Noise", "Don Delillo")
    assert str(book) == "Book(1, White Noise, Don Delillo)"


# I want to test that two identical books can be compared as equal ==
def test_same_books_compared_as_equal():
    book1 = Book(1, "White Noise", "Don Delillo")
    book2 = Book(1, "White Noise", "Don Delillo")
    assert book1 == book2