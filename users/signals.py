from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver

from orders.models import *
from .models import *

#for profiles
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()

#for orders
@receiver(post_save, sender=Orders)
def create_user_order(sender, instance, created, **kwargs):
    if created:
        User_Order.objects.create(order=instance)


@receiver(post_save, sender=Orders)
def save_user_order(sender, instance, **kwargs):
    instance.user_order.save()