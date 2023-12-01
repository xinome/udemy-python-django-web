import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ModelProject.settings')
from django import setup
setup()

from ModelApp.models import Person

# 全件取得
persons = Person.objects.all()
for person in persons:
  print(person.id, person, person.salary)

print('------------------------')

# 1件取得
# person = Person.objects.get(first_name='Taro')
person = Person.objects.get(id=1)
print(person.id, person, person.salary)

print('------------------------')

# filterメソッド（絞り込み、エラーにならない、複数取得可能）
persons = Person.objects.filter(first_name='Jiro')
print(persons)

