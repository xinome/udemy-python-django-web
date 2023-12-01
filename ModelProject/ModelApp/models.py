from django.db import models
from django.utils import timezone

# Create your models here.

# classはテーブルを作成するためのクラス
class Person(models.Model):
  first_name = models.CharField(max_length=30)
  last_name = models.CharField(max_length=30)
  birthday = models.DateField(default='1900-01-01')
  email = models.EmailField(db_index=True)  # db_index=Trueでインデックスを作成
  salary = models.FloatField(null=True)
  memo = models.TextField()
  web_site = models.URLField(null=True, blank=True)  # null=TrueでNULLを許可, blank=Trueで空文字を許可
  create_at = models.DateTimeField(default=timezone.now)
  
