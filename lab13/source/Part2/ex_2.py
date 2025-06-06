class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        
    @classmethod
    def from_string(cls, input: str) -> "Book":
        tokens = input.split(";")
        return cls(tokens[0], tokens[1])
    
# a)
book = Book.from_string("1984;George Orwell")

# b)
print(f"Book characteristics: {book.title}, {book.author}")