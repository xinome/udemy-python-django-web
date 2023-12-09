from django.urls import path
from . import views

app_name = 'form_app'

urlpatterns = [
  path('insert_student', views.insert_student, name='insert_student'),
  path('students_list', views.students_list, name='students_list'),
]

