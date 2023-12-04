import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ModelProject.settings')
from django import setup
setup()

from ModelApp.models import Students, Schools

# for student in Students.objects.all():
#   print(student.name, student.school.name, student.school.prefecture.name)
#   print('---------------------')

# 外部テーブルを参照してフィルタリング
# for student in Students.objects.filter(school__name='南高校'):
#   print(student.name, student.school.name, student.school.prefecture.name)
#   print('---------------------')

# 外部テーブルを参照してフィルタリング（除外）
# for student in Students.objects.exclude(school__name='南高校'):
#   print(student.name, student.school.name, student.school.prefecture.name)
#   print('---------------------')


print(Schools.objects.filter(students__name='太郎').all().query)

# 順番を指定して取得（ORDER BY）
for student in Students.objects.order_by('-school__name').all():
  print(student.name, student.school.name)
  print('---------------------')


# GROUP BY
from django.db.models import Count
print(Students.objects.values('school__name').annotate(Count('id')))
