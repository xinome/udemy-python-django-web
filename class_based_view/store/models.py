from django.db import models

# Create your models here.
class BaseModel(models.Model):
  created_at = models.DateTimeField()
  updated_at = models.DateTimeField()

  class Meta:
    abstract = True

class Books(BaseModel):
  name = models.CharField(max_length=255)
  description = models.CharField(max_length=1000)
  price = models.IntegerField()

  class Meta:
    db_table = 'books'

