from .models import Students
from django import forms

# メンバー追加フォーム
class StudentInsertForm(forms.ModelForm):
  name = forms.CharField(label='名前')
  age = forms.IntegerField(label='年齢')
  grade = forms.IntegerField(label='学年')
  picture = forms.FileField(label='ファイルアップロード')

  class Meta:
    model = Students
    fields = '__all__'


# メンバー編集フォーム
class StudentUpdateForm(forms.Form):
  name = forms.CharField(label='名前')
  age = forms.IntegerField(label='年齢')
  grade = forms.IntegerField(label='学年')
  picture = forms.FileField(label='ファイルアップロード')

  class Meta:
    model = Students
    fields = '__all__'