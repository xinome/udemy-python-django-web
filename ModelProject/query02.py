import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ModelProject.settings')
from django import setup
setup()

from ModelApp.models import Students, Person
# print(Students.objects.all())

ids = [13, 14, 15]
# print(Students.objects.filter(id__in=ids).all())

# contains 部分一致
# print(Students.objects.filter(name__contains='三').all().query)

# isnull NULLのみ取得
# p = Person(
#   first_name='Taro', last_name='Yamada',
#   birthday='2000-10-31', email='taro@yamada',
#   salary=1000, memo='memo taro', web_site='https://www.google.com/'
# )
# p.save()

# print(Person.objects.filter(salary__isnull=True).all().query)
# print(Person.objects.filter(salary__isnull=True).all())

# レコードを取り除く（dilter => exclude）
# print(Person.objects.exclude(salary__isnull=True).all().query)
# print(Person.objects.exclude(salary__isnull=True).all())

# 一部のカラムを取り除く
# print(Students.objects.values('name', 'age').all())

# students = Students.objects.values('id', 'name', 'age').all()
# for student in students:
#   print(student['id'])

# 並び替え
print(Person.objects.order_by('salary').all())

