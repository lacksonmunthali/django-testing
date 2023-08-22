from django.shortcuts import render
from django.http import HttpResponse
from . models import Book, Genre

# Create your views here.
def home(request):
    genres = Genre.objects.all()
    context = {"genres":genres}
    return render(request, 'index.html', context)


def genre(request, id):
    genre = Genre.objects.get(id=id)
    books = Book.objects.filter(genre=id)
    context = {"genre":genre, "books":books}
    return render(request, "genre.html", context)


def viewBook(request, id):
    book = Book.objects.get(pk=id)
    genres = book.genre.all()
    return render(request, "book.html", {"book":book, "genres":genres})

    
def greet(request):
    return HttpResponse("Hello Stanley Munga")