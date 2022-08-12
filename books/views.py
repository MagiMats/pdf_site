from django.shortcuts import render
from django.urls import reverse_lazy

from .forms import BookForm

from .models import Book
from users.models import CustomUser 

# Create your views here.
def AddBookView(request):
    if request.method == 'POST':    
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data['name']
            file = form.cleaned_data['file']
            book = Book.objects.create(file = file, name=name, owner = CustomUser.objects.get(id=request.user.id))

            return render(request, 'succes.html')
        else:
            field_errors = [(field.label, field.errors) for field in form]
            print(field_errors)
    else:
        form = BookForm()
    return render(request, 'add_book.html', {'form': form})
