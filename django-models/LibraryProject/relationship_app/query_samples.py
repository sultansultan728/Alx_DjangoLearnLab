from relationship_app.models import Author, Book, Library, Librarian

def create_sample_data():
    author1 = Author.objects.create(name="J.K. Rowling")
    author2 = Author.objects.create(name="George R.R. Martin")

    book1 = Book.objects.filter(title="Harry Potter and the Philosopher's Stone", author=author1)
    book2 = Book.objects.filter(title="Harry Potter and the Chamber of Secrets", author=author1)
    book3 = Book.objects.filter(title="A Game of Thrones", author=author2)

    library1 = Library.objects.create(name="Central Library")
    library2 = Library.objects.create(name="Community Library")

    library1.books.add(book1, book2)
    library2.books.add(book2, book3)

    Librarian.objects.create(name="Alice Johnson", library=library1)
    Librarian.objects.create(name="Bob Smith", library=library2)

    print("✅ Sample data created successfully!")


def query_books_by_author(author_name):
    author = Author.objects.get(name=author_name)
    books = author.books.all()
    print(f"📚 Books by {author.name}: {[book.title for book in books]}")


def query_books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    books = library.books.all()
    print(f"🏛️ Books in {library.name}: {[book.title for book in books]}")


def query_librarian_for_library(library_name):
    library = Library.objects.get(name=library_name)
    librarian = library.librarian
    print(f"👩‍🏫 Librarian for {library.name}: {librarian.name}")

