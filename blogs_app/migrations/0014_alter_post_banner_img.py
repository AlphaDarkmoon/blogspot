# Generated by Django 4.1.2 on 2023-09-05 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs_app', '0013_remove_profile_github'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='banner_img',
            field=models.ImageField(blank=True, null=True, upload_to='images/blogs/blogs_banner'),
        ),
    ]
