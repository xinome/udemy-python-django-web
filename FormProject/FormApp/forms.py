from django import forms
from django.core import validators
from .models import Post, ModelSetPost

class UserInfo(forms.Form):
  name = forms.CharField(label='名前', max_length=10)
  age = forms.IntegerField(label='年齢', validators=[
    validators.MinValueValidator(20, message='20歳以上でお願いします'),
    validators.MaxValueValidator(80, message='80歳以下でお願いします'),
  ])
  mail = forms.EmailField(
    label='メールアドレス',
    widget=forms.TextInput(attrs={'class': 'mail_class', 'placeholder': 'sample@mail.com'})
  )

  is_married = forms.BooleanField(initial=True)
  birthday = forms.DateField(initial='1990-01-01')
  salary = forms.DecimalField()
  job = forms.ChoiceField(choices=(
    (1, '正社員'), (2, '自営業'), (3, '学生'), (4, '無職')
  ), widget=forms.RadioSelect)
  hobby = forms.MultipleChoiceField(choices=(
    (1, 'スポーツ'), (2, '読書'), (3, '映画鑑賞'), (4, 'その他')
  ), widget=forms.CheckboxSelectMultiple)
  homepage = forms.URLField(required=False)
  memo = forms.CharField(widget=forms.Textarea, required=False)

# コンストラクタでスタイルを指定
def __init__(self, *args, **kwargs):
  super(UserInfo, self).__init__(*args, **kwargs)
  self.fields['job'].widget.attrs['id'] = 'id_job'
  self.fields['hobbies'].widget.attrs['class'] = 'class_hobbies'

# バリデーション
def clean_homepage(self):
  homepage = self.cleaned_data['homepage']
  if not homepage.startswith('https'):
    raise forms.ValidationError('httpsから始めてください')

  return homepage

class BaseForm(forms.ModelForm):
  def save(self, *args, **kwargs):
    print(f'Form: {self.__class__.__name__}のsaveメソッドが呼ばれました')
    return super(BaseForm, self).save(*args, **kwargs)

# BaseFormを継承したPostModelForm
class PostModelForm(BaseForm):

  name = forms.CharField(label='名前')
  title = forms.CharField(label='タイトル')
  memo = forms.CharField(
    label='メモ',
    widget=forms.Textarea(attrs={'rows': 30, 'cols': 20})
  )

  class Meta:
    model = Post
    fields = '__all__'
    # fields = ['name', 'title']
    # exvlude = ['title']

  # saveメソッドをオーバーライド
  def save(self, *args, **kwargs):
    # super()で親クラスのsaveメソッドを呼び出す
    obj = super(PostModelForm, self).save(commit=False, *args, **kwargs)
    obj.name = obj.name.upper()
    obj.save()

    return obj

  def clean_name(self):
    name = self.cleaned_data.get('name')
    if name == 'ああああ':
      raise validators.ValidationError('名前が登録できません')

    return name

  def clean_title(self):
    title = self.cleaned_data.get('title')
    if title == 'ああああ':
      raise validators.ValidationError('名前が登録できません')

    return title

  def clean_memo(self):
    memo = self.cleaned_data.get('memo')
    if memo == 'ああああ':
      raise validators.ValidationError('名前が登録できません')

    return memo

  def clean(self):
    cleaned_data = super().clean()
    title = cleaned_data.get('title')
    is_exists = Post.objects.filter(title=title).first()
    if is_exists:
      raise validators.ValidationError('タイトルが重複しています')

# フォームセット用のフォーム
class FormSetPost(forms.Form):
  title = forms.CharField(label='タイトル')
  memo = forms.CharField(label='メモ')
  
# モデルフォームセット用のフォーム
class ModelFormSetPost(forms.ModelForm):
  title = forms.CharField(label='タイトル')
  memo = forms.CharField(label='メモ')

  class Meta:
    model = ModelSetPost
    fields = '__all__'