from django.shortcuts import render, redirect
from p_library.models import Book, Publishing_house
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def books_list(request):
    template = loader.get_template('title.html')
    return HttpResponse(template.render())

def index(request):
    template = loader.get_template('index.html')
    books = Book.objects.all()
    numbers = []
    for i in range(1, 100):
        numbers.append(i)
    biblio_data = {
        "title": "мою библиотеку",
        "books": books,
        "numbers": numbers,
    }
    return HttpResponse(template.render(biblio_data, request))

def book_increment(request):
    if request.method == 'POST':
        book_id = request.POST['id']
        if not book_id:
            return redirect('/index/')
        else:
            book = Book.objects.filter(id=book_id).first()
            if not book:
                return redirect('/index/')
            book.copy_count += 1
            book.save()
        return redirect('/index/')
    else:
        return redirect('/index/')

def book_decrement(request):
    if request.method == 'POST':
        book_id = request.POST['id']
        if not book_id:
            return redirect('/index/')
        else:
            book = Book.objects.filter(id=book_id).first()
            if not book:
                return redirect('/index/')
            if book.copy_count < 1:
                book.copy_count = 0
            else:
                book.copy_count -= 1
            book.save()
        return redirect('/index/')
    else:
        return redirect('/index/')

def publishing_house(request):
    template = loader.get_template('publishing_house.html')
    books = Book.objects.all()
    houses = Publishing_house.objects.all()

    biblio_data = {
        "title": "мою библиотеку",
        "books": books,
        "houses": houses,
    }
    return HttpResponse(template.render(biblio_data, request))