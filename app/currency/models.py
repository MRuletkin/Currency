from currency import model_choices as mch

from django.db import models
from django.templatetags.static import static


def avatar_upload_to(instance, filename):
    return f'avatars/{instance.id}/{filename}'


class Rate(models.Model):
    buy = models.DecimalField(max_digits=6, decimal_places=2)
    sale = models.DecimalField(max_digits=6, decimal_places=2)
    created = models.DateField(auto_now_add=True)
    type = models.PositiveSmallIntegerField(  # noqa: A003
        choices=mch.RateTypeChoices.choices,
        default=mch.RateTypeChoices.USD,
    )
    source = models.ForeignKey('currency.Source', on_delete=models.CASCADE)


class ContactUs(models.Model):
    class Meta:
        verbose_name = 'Contact Us'
        verbose_name_plural = 'Contact Us'

    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=128)
    reply_to = models.EmailField()
    subject = models.CharField(max_length=128)
    body = models.CharField(max_length=1024)
    raw_content = models.TextField()


class Source(models.Model):
    source_url = models.CharField(max_length=255)
    name = models.CharField(max_length=64)
    created = models.DateTimeField(auto_now_add=True)
    avatar = models.FileField(
        upload_to=avatar_upload_to,
        default=None,
        null=True,
        blank=True,
    )
    code_name = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return self.name

    @property
    def avatar_url(self):
        if self.avatar:
            return self.avatar.url
        return static('images/default-avatar.jpg')


class RequestResponseLog(models.Model):
    path = models.CharField(max_length=255)
    request_method = models.CharField(max_length=255)
    time = models.DecimalField(max_digits=6, decimal_places=4)

# def save(self, *args, **kwargs):
#     if not self.created:
#         self.created = datetime.now()
#     return super().save(*args, **kwargs)
