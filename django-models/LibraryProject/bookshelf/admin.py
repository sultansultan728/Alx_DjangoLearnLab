from django.contrib import admin
from .models import Book

# Basic registration
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    # Columns displayed in the list view
    list_display = ('title', 'author', 'publication_year')

    # Filter sidebar for easy navigation
    list_filter = ('author', 'publication_year')

    #Search box functionality
    search_fields = ('title', 'author')
