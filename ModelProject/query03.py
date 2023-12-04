import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ModelProject.settings')
from django import setup
setup()

from ModelApp.models import Students

# print(Students.objects.all())

# 件数を取得
print(Students.objects.all().count())
print(Students.objects.filter(name='太郎').count())

# 件数、最大値、最小値、平均値、合計値
from django.db.models import Count, Max, Min, Avg, Sum
# print(Students.objects.all().aggregate(Count('pk'), Max('pk'), Min('pk'), Avg('pk'), Sum('age')))

# 変数に格納して取得
# aggregate_student = Students.objects.all().aggregate(
#   Count('pk'), Max('pk'), Min('pk'), Avg('pk'), Sum('age')
# )
# print(aggregate_student['pk__max'])

# 名前をつけて取得
# aggregate_student_named = Students.objects.all().aggregate(
#   counted_pk=Count('pk'), max_pk=Max('pk'), min_pk=Min('pk'), avg_pk=Avg('pk'), sum_age=Sum('age')
# )
# print(aggregate_student_named['sum_age'])


# GROUP BY
print(Students.objects.values('name').annotate(
  Max('pk'), Min('pk')
))

print(Students.objects.values('name', 'age').annotate(
  max_id=Max('pk'), min_id=Min('pk')
))

for student in Students.objects.values('name', 'age').annotate(
  max_id=Max('pk'), min_id=Min('pk')
):
  print(student['name'], student['max_id'])

