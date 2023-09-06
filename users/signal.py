# signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from blogs_app.models import Profile
from .models import CustomUser

@receiver(post_save, sender=CustomUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=CustomUser)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

from django.db.models.signals import post_save
from django.dispatch import receiver


