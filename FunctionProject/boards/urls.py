from django.urls import path
from . import views

app_name = 'boards'

urlpatterns = [
  path('create_theme', views.create_theme, name='create_theme'),
  path('list_themes', views.list_themes, name='list_themes'),
  path('edit_theme/<int:id>', views.edit_theme, name='edit_theme'),
  path('delete_theme/<int:id>', views.delete_theme, name='delete_theme'),
]
