import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ModelProject.settings')
from django import setup
setup()

from ModelApp.models import Person
from django.utils import timezone
# import pytz

# getメソッドを使った更新
person = Person.objects.get(id=1)
print(person)
person.birthday = '2001-01-01'
person.update_at = timezone.datetime.now()
# person.update_at = timezone.datetime.now(pytz.timezone('Asia/Tokyo'))
person.save()

# filterメソッドを使った更新
persons = Person.objects.filter(first_name='Jiro')
for person in persons:
  print(person)
  person.first_name = person.first_name.lower()
  person.update_at = timezone.datetime.now()
  person.save()

Person.objects.filter(first_name='Saburo').update(
  web_site='https://www.yahoo.co.jp/',
  # update_at=timezone.datetime.now()
)
