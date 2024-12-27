from django.shortcuts import render
from .models import *
from django.views import View
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.urls import reverse_lazy


class List_View(ListView):
    model = BookModel
    template_name = "book_list.html"
    context_object_name = 'books'


class BookCreateView(CreateView):
    model = BookModel
    fields = '__all__'
    template_name = 'book_form.html'
    success_url = reverse_lazy('book-list')

class BookUpdateView(UpdateView):
    model = BookModel
    fields = '__all__'
    template_name = 'book_form.html'
    success_url = reverse_lazy('book-list')

class BookDeleteView(DeleteView):
    model = BookModel
    template_name = 'book_delete.html'
    success_url = reverse_lazy('book-list')
    context_object_name = 'book'