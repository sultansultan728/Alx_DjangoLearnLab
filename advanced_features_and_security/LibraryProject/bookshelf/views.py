from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from .models import Book
from .forms import SearchForm
from .forms import ExampleForm


@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, "books/book_list.html", {"books": books})

@permission_required('bookshelf.can_view', raise_exception=True)
def books(request):
    form = SearchForm(request.GET or None)
    books = Book.objects.all()

    if form.is_valid():  # prevents malicious inputs
        query = form.cleaned_data["search"]
        if query:
            books = books.filter(title__icontains=query)  # ORM prevents SQL injection

    return render(
        request,
        "bookshelf/book_list.html",
        {"books": books, "form": form}
    )

@permission_required('bookshelf.can_create', raise_exception=True)
def create_book(request):
    if request.method == "POST":
        Book.objects.create(
            title=request.POST.get("title"),
            author=request.POST.get("author")
        )
        return redirect("book_list")
    return render(request, "books/create_book.html")


@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == "POST":
        book.title = request.POST.get("title")
        book.author = request.POST.get("author")
        book.save()
        return redirect("book_list")
    return render(request, "books/edit_book.html", {"book": book})


@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == "POST":
        book.delete()
        return redirect("book_list")
    return render(request, "books/delete_book.html", {"book": book})

