from django.shortcuts import render
from . import forms
from .models import Students

# Create your views here.

def insert_student(request):
  insert_form = forms.StudentInsertForm(request.POST or None, request.FILES or None)
  if insert_form.is_valid():
    insert_form.save()
    insert_form = forms.StudentInsertForm()

  return render(request, 'form_app/insert_student.html', context={
    'insert_form': insert_form
  })


def students_list(request):
  students = Students.objects.all()
  return render(request, 'form_app/students_list.html', context={
    'students': students
  })

def update_student(request, id):
  student = Students.objects.get(id=id)
  update_form = forms.StudentUpdateForm(
    initial = {
      'name': student.name,
      'age': student.age,
      'grade': student.grade,
      'picture': student.picture
    }
  )

  if request.method == 'POST':
    pass

  # if update_form.is_valid():
  #   update_form.save()
  #   update_form = forms.StudentUpdateForm(instance=student)

  return render(request, 'form_app/update_student.html', context={
    'update_form': update_form,
    'student': student
  })