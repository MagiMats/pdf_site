from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .models import Book

# Create your views here.
class AddBookView(CreateView):
    model = Book
    success_url = reverse_lazy('succes')
    template_name = 'add_book.html'
