# Generated by Django 4.1 on 2022-09-28 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0002_todolist_date_todolist_isfinished'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todolist',
            name='date',
            field=models.DateField(),
        ),
    ]
