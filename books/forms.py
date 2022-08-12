from socket import fromshare
from django import forms
from .models import Book

from django.forms import inlineformset_factory

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['name', 'file']

class AdminBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['owner','name', 'file']

class BookUserInlineFormset = inlineformset_factory (
    Book,
    CustomUser,
    form =
)
