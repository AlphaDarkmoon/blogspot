# Generated by Django 4.1.2 on 2023-09-06 07:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_customuser_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='name',
        ),
    ]
