from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model
from .forms import UserCreationForm, UserChangeForm

# カスタマイズモデル
from .models import Students, Schools

# Register your models here.

User = get_user_model()

class CustomizeUserAdmin(UserAdmin):
  form = UserChangeForm  # ユーザー編集画面で使用するフォーム
  add_form = UserCreationForm  # ユーザー作成画面

  # ユーザー一覧画面で表示する項目
  list_display = ('username', 'email', 'is_staff')

  # ユーザー編集画面で表示する項目
  fieldsets = (
    ('ユーザ情報', {'fields': ('username', 'email', 'password', 'website', 'picture')}),
    ('パーミッション', {'fields': ('is_staff', 'is_active', 'is_superuser')}),
  )

  add_fieldsets = (
    ('ユーザ情報', {
      'fields': ('username', 'email', 'password', 'confirm_password')
    }),
  )

# adminサイトでユーザーを管理できるようにする
admin.site.register(User, CustomizeUserAdmin)
# admin.site.register(Students)
admin.site.register(Schools)

@admin.register(Students)
class StudentAdmin(admin.ModelAdmin):
  # 一覧画面で表示する項目
  fields = ('name', 'score', 'age', 'school')
  list_display = ('id', 'name', 'age', 'score', 'school')
  list_display_links = ('name', )  # 一覧画面でリンクにする項目、タプルは最後にカンマをつける

  # 一覧画面で検索、フィルターする項目
  search_fields = ('name', 'age')
  list_filter = ('name', 'age', 'school', 'score')

  # 一覧画面で編集可能にする項目、リンク指定した項目は編集不可
  list_editable = ('age', 'score')
