# Generated by Django 4.2.4 on 2023-09-04 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs_app', '0009_alter_post_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='snippet',
            field=models.CharField(default='...', max_length=255),
        ),
    ]
