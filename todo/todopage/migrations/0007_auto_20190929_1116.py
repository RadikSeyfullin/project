# Generated by Django 2.2.5 on 2019-09-29 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todopage', '0006_auto_20190926_2121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todolist',
            name='created',
            field=models.DateField(default='2019-09-29'),
        ),
        migrations.AlterField(
            model_name='todolist',
            name='due_date',
            field=models.DateField(default='2019-09-29'),
        ),
    ]