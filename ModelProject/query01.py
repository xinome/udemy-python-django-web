import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ModelProject.settings')
from django import setup
setup()

from ModelApp.models import Students

# 全件取得
# print(Students.objects.all())

# 先頭5件取得
# print(Students.objects.all()[:5])

# 5件目以降を取得
# print(Students.objects.all()[5:])

# 5~7件目を取得
# print(Students.objects.all()[5:8])
# クエリ文字列を確認
# print(Students.objects.all()[5:8].query)

# 1番最初のレコードを取得
# print(Students.objects.first())

# 等価のものだけを取得
# print(Students.objects.filter(name='太郎').all())

# AND条件
# print(Students.objects.filter(name='太郎', pk__gt=13).all().query)

# 全件一致、後方一致
print(Students.objects.filter(name__startswith='太').all().query)
print(Students.objects.filter(name__endswith='郎').all().query)

# OR条件
from django.db.models import Q
print(Students.objects.filter(Q(name='太郎') | Q(name='次郎')).all().query)





