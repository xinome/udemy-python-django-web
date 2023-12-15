from django.shortcuts import render, redirect
from .models import Items

# Create your views here.

def item_list(request):
  items = Items.objects.all()
  return render(request, 'store/item_list.html', context={
    'items': items
  })

def item_detail(request, id):
  item = Items.objects.get(id=id)
  return render(request, 'store/item_detail.html', context={
    'item': item
  })

def to_google(request):
  return redirect('https://www.google.com/')

# 特定の商品の詳細ページにリダイレクトする
def one_item(request):
  return redirect('store:item_detail', id=1)