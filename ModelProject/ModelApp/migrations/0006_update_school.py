# Generated by Django 4.1 on 2023-12-04 09:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ModelApp', '0005_add_author_book'),
    ]

    operations = [
        migrations.RenameField(
            model_name='schools',
            old_name='prefecuture',
            new_name='prefecture',
        ),
    ]
