from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Book, Author
from django.contrib.auth.decorators import login_required
from .forms import NewBookForm
# Create your views here.

# books = [
#     { 'id': 1, 'title': 'Life, the Universe and Everything', 'author': 'Douglas Adams'},
#     { 'id': 2, 'title': 'The Meaning of Liff', 'author': 'Douglas Adams'},
#     { 'id': 3, 'title': 'The No. 1 Ladies\' Detective Agency', 'author': 'Alexander McCall Smith'}
# ]

def index(request):
    data = {
        "books": Book.objects.all()
    }
    return render(request, "index.html", data)

@login_required
def show(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    # book = list(filter(lambda b: b["id"] == book_id, books))[0]
    data = {
        "book": book
    }
    return render(request, "show.html", data)

def not_found_404(request, exception):
    data = {
        "message": exception
    }
    return render(request, "404.html",data)

@login_required
def new(request):
    if request.method == "POST":
        book = NewBookForm(request.POST)
        if book.is_valid():
            id = book.save().id
            return redirect("books-show", book_id=id)
    else:
        form = NewBookForm()
    data = {"form": form}
    return render(request, "new.html", data)