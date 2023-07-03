from django.urls import path, include
from book import views 

urlpatterns = [
    path('', views.index , name = 'index'),
    path('author_form/', views.author_form, name = "author"),
    path('book_form/', views.book_form, name = "book"),
    path('author/add_author/', views.add_author, name='add_author'),
    path('book/add_book/', views.add_book, name = "add_book"),
    path('author=', views.books_by_author, name = "books_by_author")
]