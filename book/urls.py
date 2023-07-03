from django.urls import path, include, re_path
from book import views 

urlpatterns = [
    path('', views.index , name = 'index'),
    path('author_form/', views.author_form, name = "author"),
    path('book_form/', views.book_form, name = "book"),
    path('author_form/add_author/', views.add_author, name='add_author'),
    path('book_form/add_book/', views.add_book, name = "add_book"),
    path('author=<str:author>', views.books_by_author, name = "books_by_author"),
    path('<str:title>', views.get_book, name= "get_book")
]