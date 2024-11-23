from django.shortcuts import render, redirect, get_object_or_404
from .models import Book
from .forms import BookForm

'''
ლინკების დამატება დამეზარა და ვერ გავიგე objects.create ით უნდა გამეკეთებინა თუ როგორც ადრე, მაგრამ objects.create ით მაინც ვერ გავიგე როგორ მექნა
'''



def books(request):
    books = Book.objects.filter(rating__gt=6)
    return render(request, 'books.html', context={'books': books})

def create_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('books')
    else:
        form = BookForm()
    return render(request, 'create_book.html', {'form': form})

def update_book(request, id):
    books = get_object_or_404(Book, id=id)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=books)
        if form.is_valid():
            form.save()
            return redirect('books')
    else:
        form = BookForm(instance=books)
    return render(request, 'update_book.html', {'form': form})

def detail_book(request, id):
    book = Book.objects.get(id=id)
    return render(request, 'detail_book.html', {'book': book})

def delete_book(request, id):
    Book.objects.get(id=id).delete()
    return redirect('books')