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

def sample(request):
  name = 'ichiro yamada'
  height = 175.5
  weight = 72
  bmi = weight / (height/100) ** 2
  page_url = 'ホームページ: https://www.google.com/'
  favorite_fruits = ['apple', 'banana', 'orange']
  msg = """hello
  my name is 
  ichiro
  """
  msg2 = '1234567890'

  return render(request, 'sample.html', context={
    'name': name,
    'height': height,
    'weight': weight,
    'bmi': bmi,
    'page_url': page_url,
    'favorite_fruits': favorite_fruits,
    'msg': msg,
    'msg2': msg2,
  })
