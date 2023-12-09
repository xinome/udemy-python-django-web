from django.shortcuts import render
from django.forms import formset_factory, modelformset_factory
from . import forms
from .models import ModelSetPost
from django.core.files.storage import FileSystemStorage
import os

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

# フォームセット
def form_set_post(request):
  TestFormset = formset_factory(forms.FormSetPost, extra=3)
  formset = TestFormset(request.POST or None)
  if formset.is_valid():
    for form in formset:
      print(form.cleaned_data)

  return render(
    request, 'formapp/form_set_post.html', context={'formset': formset}
  )

# モデルフォームセット
def modelform_set_post(request):
  # TestFormset = modelformset_factory(ModelSetPost, fields='__all__', extra=3)
  TestFormset = modelformset_factory(ModelSetPost, form=forms.ModelFormSetPost, extra=3)
  formset = TestFormset(request.POST or None, queryset=ModelSetPost.objects.filter(id__gt=3))
  if formset.is_valid():
    formset.save()

  return render(
    request, 'formapp/modelform_set_post.html', context={'formset': formset}
  )

# アップロードファイル
def upload_sample(request):
  if request.method == 'POST' and request.FILES['file']:
    # 送られたファイルの取り出し
    upload_file = request.FILES['upload_files']
    fs = FileSystemStorage()  # ファイルを保存する
    file_path = os.path.join('upload', upload_file.name)
    file = fs.save(file_path, upload_file)
    uploaded_file_url = fs.url(file)

    return render(request, 'formapp/upload_file.html', context={
      'uploaded_file_url': uploaded_file_url
    })

  return render(request, 'formapp/upload_file.html')
