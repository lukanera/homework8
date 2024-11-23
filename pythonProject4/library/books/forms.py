from django.forms import ModelForm
from .models import Book, Author, Category

class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'description', 'author', 'category', 'rating']

class AuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = ['name']

class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ['name']