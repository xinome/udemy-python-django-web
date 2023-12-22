from django.db import models
from django.contrib.auth.models import (
  AbstractBaseUser,
  PermissionsMixin,
)

from django.db.models.signals import post_save
from django.dispatch import receiver
from uuid import uuid4
from datetime import datetime, timedelta

# Create your models here.

class Users(AbstractBaseUser, PermissionsMixin):
  username = models.CharField(max_length=255)
  age = models.PositiveIntegerField()
  email = models.EmailField(max_length=255, unique=True)
  is_active = models.BooleanField(default=False)
  is_staff = models.BooleanField(default=False)
  picture = models.FileField(null=True, upload_to='picture/')

  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = ['username']

  class Meta:
    db_table = 'users'

class UserActivateTokens(models.Model):
  token = models.UUIDField(db_index=True)
  expired_at = models.DateTimeField()
  user = models.ForeignKey(
    'Users', on_delete=models.CASCADE
  )

  class Meta:
    db_table = 'user_activate_tokens'

# シグナルを使って、ユーザー登録時にUserActivateTokensモデルにレコードを作成する
@receiver(post_save, sender=Users)
def publish_token(sender, instance, **kwargs):
  print(str(uuid4()))
  print(datetime.now() + timedelta(days=1))

  user_activate_token = UserActivateTokens.objects.create(
    user=instance,
    token=str(uuid4()),
    expired_at=datetime.now() + timedelta(days=1)
  )

  # 本来メールでユーザー登録用のURLを送信する部分
  print(f'http://localhost:8000/accounts/activate_user/{user_activate_token.token}')
