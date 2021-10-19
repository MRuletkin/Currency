from django.db import models


class Rate(models.Model):
    buy = models.DecimalField(max_digits=6, decimal_places=2)
    sale = models.DecimalField(max_digits=6, decimal_places=2)
    created = models.DateTimeField()
    type = models.CharField(max_length=3)  # noqa: A003
    source = models.CharField(max_length=25)


class ContactUs(models.Model):
    id = models.AutoField(primary_key=True)
    email_from = models.EmailField(max_length=254)
    subject = models.CharField(max_length=50)
    message = models.CharField(max_length=100)
