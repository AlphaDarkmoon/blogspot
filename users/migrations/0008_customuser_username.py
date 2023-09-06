# Generated by Django 4.1.2 on 2023-09-06 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_remove_customuser_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='username',
            field=models.EmailField(default='username', max_length=254, unique=True, verbose_name='User Name'),
        ),
    ]