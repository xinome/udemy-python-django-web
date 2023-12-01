import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ModelProject.settings')
from django import setup
setup()

from ModelApp.models import Person

# 削除メソッド
Person.objects.get(first_name='Saburo').delete()

# id=1のデータを削除
Person.objects.filter(id=1).delete()

# 全件削除
Person.objects.all().delete()