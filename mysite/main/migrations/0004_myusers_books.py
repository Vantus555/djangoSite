# Generated by Django 4.0.4 on 2022-05-18 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_book_year'),
    ]

    operations = [
        migrations.AddField(
            model_name='myusers',
            name='books',
            field=models.ManyToManyField(to='main.book'),
        ),
    ]
