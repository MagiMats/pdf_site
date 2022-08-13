from django.shortcuts import render
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required

from .forms import BookForm

from .models import Book
from users.models import CustomUser 

import fitz 
# Create your views here.
def AddBookView(request):
    if request.method == 'POST':    
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data['name']
            file = form.cleaned_data['file']
            
            book = Book.objects.create(file = file, name=name, owner = CustomUser.objects.get(id=request.user.id))

            return render(request, 'succes.html', {'book': name})
        else:
            field_errors = [(field.label, field.errors) for field in form]
            print(field_errors)
    else:
        form = BookForm()
    return render(request, 'add_book.html', {'form': form})

@login_required
def BookList(request):
    user = request.user
    books = Book.objects.filter(owner = CustomUser.objects.get(id=request.user.id))
    return render(request, 'book_list.html', {'user': user, 'books': books})

def BookDetail(request, book_id):
    book_file = Book.objects.get(id=book_id)
    book = fitz.open(book_file.file)
    toc = book.get_toc()
    return render(request, 'book_detail.html', {'book_file': book_file.file, 'toc': toc})

