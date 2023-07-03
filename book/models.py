from django.db import models
import uuid

# Create your models here.

# Create a Django view for a bookstore application that retrieves a list of books from the
# database and returns the book titles, authors, and prices. Implement a filtering
# functionality that allows users to filter books based on a specific author's name.
# Book Model: title , author (ForeignKey to the Author model), price , publication_date,
# description, image.
# Author Model: name, biography, photo.
# 6) Create a Django model named Review to represent user reviews for books. The model
# should include the following fields:
# Review : book (ForeignKey to the Book model),content, rating (IntegerField)

# a) Implement the review submission form, including fields for the review content, and
# rating. Upon form submission, save the new review to the database with the
# appropriate association to the reviewed book.
# b) Modify the bookstore application's detail view for a book to include the book's
# detailed information and display any existing reviews.

class Author(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=255, blank= False)
    biography = models.TextField(blank= False)
    photo = models.ImageField(null=True)
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now= True)
    
    def __str__(self):
        return self.name

class Books(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    title = models.CharField(max_length=255, blank= False)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    publication_date = models.DateField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now= True)

    def __str__(self):
        return self.title
    
class Review(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    content = models.TextField(blank= False)
    book = models.ForeignKey(Books, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now= True)
    
    def __str__(self):
        return self.book
