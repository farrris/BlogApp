# Generated by Django 4.0.3 on 2022-04-07 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Title')),
                ('body', models.CharField(max_length=500, verbose_name='Body')),
                ('date', models.CharField(max_length=20, verbose_name='Date')),
            ],
        ),
        migrations.CreateModel(
            name='Name',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(default='Это мой блог', max_length=100, verbose_name='Name')),
            ],
        ),
    ]
