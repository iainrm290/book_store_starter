# Class design

# class Book

# __init__ method
# This is initialised with attributes - id, title, author_name
# Each column in the table is reflected by these attributes
class Book:
    def __init__(self, id, title, author_name):
        self.id = id
        self.title = title
        self.author_name = author_name




# __eq__ method
# This method allows our tests to assert that the objects tested
# are considered equal to the objects from the database records
# Returns a bool

    def __eq__(self, other):
        return self.__dict__ == other.__dict__


# __repr__ method
# This method formats the record details in a readable way for the user
# Returns a formatted string f""

    def __repr__(self):
        return f"Book({self.id}, {self.title}, {self.author_name})"
