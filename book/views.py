from django.shortcuts import redirect, render
from . import models

# Create your views here.


def index(request):
    return redirect('/book/')

def all_books(request):
    books = models.Book.get_all()

    context = {
        'is_empty' : not bool(books),
        'books' : books
    }

    return render(request, 'all_books.html', context)

def book_by_id(request, id_book):
    book = models.Book.get_by_id(id_book)
    context = {
        'not_found' : (book is None),
        'id' : id_book,
        'book' : book,
    }
    return render(request, 'book_by_id.html', context)


def filter_by_author_id(request, author_id):
    author = models.Author.get_by_id(author_id)

    if author is None:
        context = {
            'no_author': True,
            'author_id': author_id,
        }
    else:
        print(author.books.all())
        books = author.books.all()
        context = {
        'no_author' : False,
        'is_empty' : not bool(books),
        'books' : books,
        'author': author,
        }


    return render(request, 'filter_by_author_id.html', context)