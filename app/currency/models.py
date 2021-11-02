from django.db import models


class Rate(models.Model):
    buy = models.DecimalField(max_digits=6, decimal_places=2)
    sale = models.DecimalField(max_digits=6, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)
    type = models.CharField(max_length=3)  # noqa: A003
    source = models.CharField(max_length=25)


class ContactUs(models.Model):
    email_from = models.EmailField(max_length=254)
    subject = models.CharField(max_length=50)
    message = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)


class Source(models.Model):
    source_url = models.CharField(max_length=255)
    name = models.CharField(max_length=64)
    created = models.DateTimeField(auto_now_add=True)


# def save(self, *args, **kwargs):
#     if not self.created:
#         self.created = datetime.now()
#     return super().save(*args, **kwargs)
