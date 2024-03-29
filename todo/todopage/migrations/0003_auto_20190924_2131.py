# Generated by Django 2.2.4 on 2019-09-24 21:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todopage', '0002_todolist_deleted'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('created', models.DateField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.AlterModelOptions(
            name='todolist',
            options={'ordering': ['-created']},
        ),
        migrations.RenameField(
            model_name='todolist',
            old_name='name',
            new_name='title',
        ),
        migrations.AddField(
            model_name='todolist',
            name='due_date',
            field=models.DateField(default='2019-09-24'),
        ),
        migrations.AlterField(
            model_name='todolist',
            name='created',
            field=models.DateField(default='2019-09-24'),
        ),
        migrations.AddField(
            model_name='todolist',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='todopage.Category'),
        ),
    ]
