from user.models import CustomUser
from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import Profile


@receiver(post_save, sender=CustomUser)
def create_profile(created, instance, sender, **kwargs):
    if created:
        Profile.objects.create(user=instance)