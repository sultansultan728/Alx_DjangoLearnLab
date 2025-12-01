from django.db import models
from django.utils import timezone

"""
Author Model
------------
Represents a writer of one or more books.
Only contains a name field, but can be expanded later.

Relationship:
One Author -> Many Books (one-to-many)
"""

class Author(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


"""
Book Model
----------
Represents a book written by an author.

Fields:
- title: title of the book
- publication_year: year book was published
- author: FK → Author (each book belongs to exactly one author)

The FK creates a one-to-many relationship handled naturally
by Django ORM and automatically available to serializers.
"""

class Book(models.Model):
    title = models.CharField(max_length=255)
    publication_year = models.IntegerField()
    author = models.ForeignKey(
        Author,
        related_name="books",
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.title} ({self.publication_year})"

