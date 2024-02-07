from django.shortcuts import render
from django.views.generic.base import (
  View, TemplateView
)
from . import forms
from datetime import datetime

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

class HomeView(TemplateView):
  template_name = 'home.html'
  
  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    print(kwargs)
    context['name'] = kwargs.get('name')
    context['time'] = datetime.now()
    
    return context
