# Generated by Django 4.2.4 on 2023-09-08 06:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs_app', '0025_subscribedusers'),
    ]

    operations = [
        migrations.DeleteModel(
            name='SubscribedUsers',
        ),
    ]
