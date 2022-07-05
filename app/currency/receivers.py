from currency import consts
from currency.models import Rate

from django.core.cache import cache
from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save, sender=Rate)
def rate_post_save_clear_cache(sender, instance, created, **kwargs):
    if created:
        cache.delete(consts.LATEST_RATE_KEY)
