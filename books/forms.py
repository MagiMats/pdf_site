from operator import attrgetter
from socket import fromshare
from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['name', 'file']
        widgets = {
            'file': forms.FileInput(attrs={'class': 'file_input'})
        }
        
class AdminBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['owner','name', 'file']

