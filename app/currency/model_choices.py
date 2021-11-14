from django.db import models


class RateTypeChoices(models.IntegerChoices):
    USD = 1, 'Dollar'
    EUR = 2, 'Euro'
    UAH = 3, 'Hryvnia'


class RateSourceChoices(models.IntegerChoices):
    PB = 1, 'Privatbank'
    MB = 2, 'Monobank'
    OB = 3, 'Oschadbank'
