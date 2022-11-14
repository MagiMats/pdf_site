from django.contrib import admin
from .models import Book
from .forms import AdminBookForm

# Register your models here.

class BookAdmin(admin.ModelAdmin):
    form = AdminBookForm
    model = Book

admin.site.register(Book, BookAdmin)


