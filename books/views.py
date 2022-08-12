from django.shortcuts import render
from django.urls import reverse_lazy

from .forms import BookForm

from .models import Book

# Create your views here.
def AddBookView(request):
    if request.method == 'POST':    
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            pass
    return render(request, 'add_book.html', {'form': form})
