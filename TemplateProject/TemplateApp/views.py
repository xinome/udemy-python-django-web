from django.shortcuts import render

# Create your views here.

def index(request):
  val = 'Good Bye'
  return render(request, 'index.html', context={'value': val})

def home(request):
  my_name = 'Taro'
  favorite_fruits = ['apple', 'banana', 'orange']
  my_info = {
    'name': 'Taro',
    'age': 18,
  }

  return render(request, 'home.html', context={
    'my_name': my_name,
    'favorite_fruits': favorite_fruits,
    'my_info': my_info,
  })

def sample1(request):
  return render(request, 'sample1.html')

def sample2(request):
  return render(request, 'sample2.html')