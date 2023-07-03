from django import forms
from django.forms import ModelForm
from book.models import Author, Books, Review

# Create a venue form
class AuthorForm(ModelForm):
	class Meta:
		model = Author
		fields = ('name', 'biography', 'photo')
		labels = {
			'name': 'Name ',
			'biography': 'Biography',
			'photo': '',			
		}
		widgets = {
			'name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Author Name'}),
			'biography': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Biography'}),
		}

class BookForm(ModelForm):
	author = forms.ModelChoiceField(queryset=Author.objects.all())
	class Meta:
		model = Books
		fields = ('title', 'author', 'price')
		labels = {
			'title': 'Title',
			'author': 'Choose Author',
			'price': 'Enter Price',			
		}
		widgets = {
			'title': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Title'}),
			'price': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Biography'}),
			'author': forms.Select(attrs={'class': 'form-control'})
		}