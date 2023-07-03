from django.shortcuts import render, HttpResponse, get_object_or_404
from django.http import JsonResponse
from .forms import AuthorForm, BookForm
from .models import Books, Author, Review

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

def books_by_author(request):
    author_name = request.GET.get('author')
    author = get_object_or_404(Author, name=author_name)
    books = Books.objects.filter(author=author)

    book_list = []
    for book in books:
        book_dict = {
            'title': book.title,
            'author': book.author.name,
            'genre': book.genre
        }
        book_list.append(book_dict)

    return JsonResponse(book_list, safe=False)