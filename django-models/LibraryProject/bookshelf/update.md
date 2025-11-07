book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()
print(book.title, book.author, book.publication_year)
# Nineteen Eighty-Four George Orwell 1949

