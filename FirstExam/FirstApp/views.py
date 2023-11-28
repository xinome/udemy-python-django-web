from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# num1とnum2を受け取って、足し算した結果を表示する
def add(request, num1, num2):
  return HttpResponse(f'<h1>{num1 + num2}</h1>')

# num1とnum2を受け取って、引き算した結果を表示する（num1とnum2は浮動小数点数で0かプラス）
def minus(request, num1, num2):
  num1 = float(num1)
  num2 = float(num2)
  return HttpResponse(f'<h1>{num1 - num2}</h1>')

# num1とnum2の値を割ったもので四捨五入したものを表示（num1とnum2は浮動小数点数で0かプラス）
def div(request, num1, num2):
  num1 = float(num1)
  num2 = float(num2)
  return HttpResponse(f'<h1>{round(num1 / num2)}</h1>')
