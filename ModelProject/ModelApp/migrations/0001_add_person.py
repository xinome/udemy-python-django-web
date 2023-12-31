# Generated by Django 4.1 on 2023-12-01 07:02

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('birthday', models.DateField(default='1900-01-01')),
                ('email', models.EmailField(db_index=True, max_length=254)),
                ('salary', models.FloatField(null=True)),
                ('memo', models.TextField()),
                ('web_site', models.URLField(blank=True, null=True)),
                # 並べ替える場合は直接編集する
                ('create_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'person',
                'ordering': ['salary'],
                'index_together': {('first_name', 'last_name')},
            },
        ),
    ]
