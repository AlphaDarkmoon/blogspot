# Generated by Django 4.2.4 on 2023-09-07 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs_app', '0022_alter_profile_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(blank=True, default='images/profile/profile_default.jpg', null=True, upload_to='images/admin/profile'),
        ),
    ]
