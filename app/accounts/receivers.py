from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from accounts.models import User


@receiver(pre_save, sender=User)
def user_pre_save(sender, instance, **kwargs):
    if instance.email:
        instance.email = instance.email.lower()


@receiver(pre_save, sender=User)
def user_pre_save_phone_field(sender, instance, **kwargs):
    if instance.phone:
        for i in instance.phone:
            if not i.isdigit():
                instance.phone = instance.phone.replace(i, '')


@receiver(post_save, sender=User)
def user_post_save(sender, **kwargs):
    print('user_post_save')
