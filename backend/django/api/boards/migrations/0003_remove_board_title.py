# Generated by Django 3.2.1 on 2021-09-28 08:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0002_board_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='board',
            name='title',
        ),
    ]
