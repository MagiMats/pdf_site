from django.urls import path
from .views import AddBookView
from django.views.generic.base import TemplateView

urlpatters = [
    path('upload', AddBookView, name='add_book'),
    path('succes', TemplateView.as_view(template_name='succes.html'),name='succes')
]