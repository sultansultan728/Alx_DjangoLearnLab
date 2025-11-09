from django.shortcuts import render
from django.views.generic import DetailView
from .models import Book, Library

# --- Function-based view to list all books ---
def list_books(request):
    books = Book.objects.select_related('author').all()
    return render(request, 'list_books.html', {'books': books})

