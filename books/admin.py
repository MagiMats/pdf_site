from django.contrib import admin
from .models import Book
from .forms import BookForm

# Register your models here.

class BookAdmin(admin.ModelAdmin):
    form = BookForm
    model = Book

admin.site.register(Book)


