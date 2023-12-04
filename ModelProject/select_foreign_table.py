import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ModelProject.settings')
from django import setup
setup()


# 1:Nの場合
from ModelApp.models import Students, Schools, Prefectures

s = Schools.objects.first()
print(s)
# print(dir(s))

# print(s.prefecture.name)
print(s.students_set.all())

# 1:1の場合
from ModelApp.models import Places, Restaurants

p = Places.objects.first()
print(type(p))
# print(dir(p))
# print(p.restaurants.name)

r = Restaurants.objects.first()
print(r.place.name)


# N:Nの場合
from ModelApp.models import Authors, Books

b = Books.objects.first()
print(b.authors.all())
a = Authors.objects.first()
print(a.books_set.all())
