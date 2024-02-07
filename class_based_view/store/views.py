from django.shortcuts import render
from django.views.generic.base import (
  View,
)
from . import forms

# Create your views here.

class IndexView(View):

  def get(self, request, *args, **kwargs):
    book_form = forms.BookForm()
    return render(request, 'index.html', context={
      'book_form': book_form,
    })

  def post(self, request, *args, **kwargs):
    book_form = forms.BookForm(request.POST)
    if book_form.is_valid():
      book_form.save()
      
    return render(request, 'index.html', context={
      'book_form': book_form,
    })

