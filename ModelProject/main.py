import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ModelProject.settings')
from django import setup
setup()

from ModelApp.models import Person

# データの追加（saveメソッド）
p = Person(
  first_name='Taro', last_name='Sato',
  birthday='2000-10-31', email='taro@yamada',
  salary=None, memo='memo taro', web_site='https://www.google.com/'
)
# p.save()

# データの追加（createメソッド）
# Person.objects.create(
#   first_name='Jiro', last_name='Ito',
#   email='jiro@yamada',
#   salary=20000, memo='class method 実行', web_site=None
# )

# データの追加（get_or_createメソッド）
obj, created = Person.objects.get_or_create(
  first_name='Saburo', last_name='Suzuki',
  email='saburo@yamada',
  salary=30000, memo='get_or_create 実行', web_site=None
)

print(obj)
print(created)