from django.shortcuts import render, redirect, get_object_or_404
from . import forms
from django.contrib import messages
from .models import Themes
from django.http import Http404

# Create your views here.
def create_theme(request):
  create_theme_form = forms.CreateThemeForm(request.POST or None)
  if create_theme_form.is_valid():
    # ここでユーザーをセットする
    create_theme_form.instance.user = request.user
    create_theme_form.save()
    messages.success(request, '掲示板を作成しました。')
    return redirect('boards:list_themes')

  return render(request, 'boards/create_theme.html', context={
    'create_theme_form': create_theme_form
  })

def list_themes(request):
  themes = Themes.objects.fetch_all_themes()
  return render(request, 'boards/list_themes.html', context={
    'themes': themes
  })

def edit_theme(request, id):
  theme = get_object_or_404(Themes, id=id)
  if theme.user_id != request.user.id:
    raise Http404
  
  edit_theme_form = forms.CreateThemeForm(request.POST or None, instance=theme)
  if edit_theme_form.is_valid():
    edit_theme_form.save()
    messages.success(request, '掲示板を更新しました。')
    return redirect('boards:list_themes')
  
  return render(request, 'boards/edit_theme.html', context={
    'edit_theme_form': edit_theme_form,
    'id': id,
  })

def delete_theme(request, id):
  theme = get_object_or_404(Themes, id=id)
  if theme.user_id != request.user.id:
    raise Http404
  
  delete_theme_form = forms.DeleteThemeForm(request.POST or None, instance=theme)
  if delete_theme_form.is_valid():  # csrf_tokenのチェック
    theme.delete()
    messages.success(request, '掲示板を削除しました。')
    return redirect('boards:list_themes')

  return render(request, 'boards/delete_theme.html', context={
    'delete_theme_form': delete_theme_form,
    'id': id,
  })

