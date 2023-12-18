from django.db import models
from django.contrib.auth.models import (
  BaseUserManager,
  AbstractBaseUser,
  PermissionsMixin
)

# Create your models here.

# マネージャーを定義
class UserManager(BaseUserManager):
  def create_user(self, username, email, password=None):
    if not email:
      raise ValueError('Enter Email!!')

    user = self.model(
      username=username,
      email=self.normalize_email(email),
    )

    user.set_password(password)
    user.save(using=self._db)
    return user

  def create_superuser(self, username, email, password=None):
    user = self. model(
      username=username,
      email=email,
    )
    
    user.set_password(password)
    user.is_staff = True
    user.is_active = True
    user.is_superuser = True
    user.save(using=self._db)
    return user
    

class User(AbstractBaseUser, PermissionsMixin):
  username = models.CharField(max_length=150)
  email = models.EmailField(max_length=255, unique=True)
  is_active = models.BooleanField(default=True)
  is_staff = models.BooleanField(default=False)
  website = models.URLField(null=True)
  picture = models.FileField(null=True)

  USERNAME_FIELD = 'email'  # このテーブルのレコードを一意に識別する
  REQUIRED_FIELDS = ['username']  # superuser作成時に必要となるフィールド

  objects = UserManager()

  def __str__(self):
    return self.email
