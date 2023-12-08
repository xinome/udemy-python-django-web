from django.shortcuts import render
from . import forms

# Create your views here.

def index(request):
  return render(request, 'formapp/index.html')

def form_page(request):
  form = forms.UserInfo()
  if request.method == 'POST':
    # Formで送られたデータを取得
    form = forms.UserInfo(request.POST)

    # バリデーションチェック
    if form.is_valid():
      # print('バリデーション成功')
      # print(
      #   f'name: {form.cleaned_data["name"]}, mail: {form.cleaned_data["mail"]}, age: {form.cleaned_data["age"]}'
      # )
      print(form.cleaned_data)

  return render(request, 'formapp/form_page.html', context={
    'form': form
  })

def form_post(request):
  form = forms.PostModelForm()

  # DBに保存
  if request.method == 'POST':
    form = forms.PostModelForm(request.POST)
    if form.is_valid():
      form.save()

  return render(
    request, 'formapp/form_post.html', context={'form': form}
  )