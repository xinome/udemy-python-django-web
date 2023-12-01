from django.db import models

# Create your models here.

# classはテーブルを作成するためのクラス
class Person(models.Model):
  first_name = models.CharField(max_length=30)
  last_name = models.CharField(max_length=30)

class Sales(models.Model):
   fee = models.IntegerField()
   created_at = models.DateTimeField()
   updated_at = models.DateTimeField()