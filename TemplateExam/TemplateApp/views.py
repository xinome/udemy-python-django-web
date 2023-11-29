from django.shortcuts import render

# Create your views here.

# メンバークラス
class Member:
  def __init__(self, id, name, join_at, picture_path):
    self.id = id
    self.name = name
    self.join_at = join_at
    self.picture_path = picture_path

# メンバー一覧
member_list = [
  Member(0, 'Taro', '2021/04/01', 'img/taro.jpg'),
  Member(1, 'Jiro', '2022/04/01', 'img/jiro.jpg'),
  Member(2, 'Hanako', '2023/04/01', 'img/hanako.jpg'),
  Member(3, 'Yoshiko', '2024/04/01', 'img/yoshiko.jpg'),
]

# ホーム画面
def home(request):
  return render(request, 'home.html')

# メンバー一覧画面
def members(request):
  return render(request, 'members.html', context={
    'members': member_list
  })

# メンバー詳細画面
def member(request, id):
  return render(request, 'member_detail.html', context={
    'member': member_list[id]
  })