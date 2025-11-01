# Retrieve Operation

```python
from bookshelf.models import Book

# Retrieve the book using the ORM
book = Book.objects.get(title="1984")

# Display the book's details
print(book.title, book.author, book.publication_year)

