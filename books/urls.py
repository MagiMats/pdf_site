from django.urls import path
from .views import AddBookView, BookDetail, BookList
from django.views.generic.base import TemplateView
from django.http import HttpResponse

urlpatterns = [
    path('upload', AddBookView, name='add_book'),
    path('succes', TemplateView.as_view(template_name='succes.html'),name='succes'),
    path('book_list', BookList, name='book_list'),
    path('book_detail/<int:book_id>/', BookDetail, name='book_detail'),
]