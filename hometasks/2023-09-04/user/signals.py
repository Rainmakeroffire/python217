from django.db.models.signals import post_save, post_delete
from .models import Profile, User
from django.dispatch.dispatcher import receiver


@receiver(post_save, sender=User)
def profile_update(sender, instance, created, **kwargs):
    if created:
        user = instance
        profile = Profile.objects.create(
            user=user,
            username=user.username,
            email=user.email,
        )


@receiver(post_delete, sender=Profile)
def delete_user(sender, instance, **kwargs):
    user = instance.user
    user.delete()
