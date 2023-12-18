# カスタムバリデーション
from django.core.exceptions import ValidationError
import re

class CustomPasswordValidator():

  def __init__(self, min_length=8):
    pass

  def validate(self, password, user=None):
    # 全ての条件を満たしているか
    if all((re.search('[0-9]', password)), (re.search('[a-z]', password)), (re.search('[A-Z]', password))):
      return
    raise ValidationError('パスワードは大文字、小文字、数字を含めてください')

  def get_help_text(self):
    return 'パスワードは大文字、小文字、数字を含めてください'