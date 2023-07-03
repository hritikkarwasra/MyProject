from django.shortcuts import render, HttpResponse, get_object_or_404
from django.http import JsonResponse
from .forms import AuthorForm, BookForm
from .models import Books, Author, Review
import json

# Create your views here.

def index(request):
    authors = Author.objects.all()
    return render(request, 'book/book.html', {'authors':authors})

def author_form(request):
    form = AuthorForm(request.POST, request.FILES)
    return render(request, 'book/add_author.html', {'form':form})

def book_form(request):
    form = BookForm(request.POST)
    return render(request, 'book/add_book.html', {'form':form})

def add_book(request):
    form = BookForm(request.POST)
    message = "Failed"
    status = 400
    try:
        if request.method == "POST":
            if form.is_valid():
                book = form.save(commit=False)
                book.save()
                message = "Success"
                status = 200	
    except Exception as e:
        print(e)
        status = 400
    return HttpResponse(message , status= status)
    
def add_author(request):
    form = AuthorForm(request.POST, request.FILES)
    message = "Failed"
    status = 400
    try:
        if request.method == "POST":
            if form.is_valid():
                author = form.save(commit=False)
                author.save()
                message = "Success"
                status = 200	
    except Exception as e:
        print(e)
        status = 400
    return HttpResponse(message , status= status)

def books_by_author(request, author):
    if request.method == 'GET':
        print(author)
        book_list = []
        author = Author.objects.filter( name= author).first()
        if author:
            books = Books.objects.filter(author=author)

            for book in books:
                book_dict = {
                    'title': book.title,
                    'author': book.author.name,
                    'price': book.price
                }
                book_list.append(book_dict)
        print(book_list)

    return JsonResponse(book_list, safe=False)

def get_book(request, title):
    context = {}
    if request.method == 'GET':
        print(title)
        lst = title.split("+")
        author_name = lst[0],
        book_title = lst[1]
        print(author_name, book_title)
        author = Author.objects.filter(name = author_name)

        book = Books.objects.filter(title = book_title).first()

        if book:
            context ={
                "book":book
            }
        
    return render(request, 'book/book_page.html', context)