from django.contrib.auth.models import User
from django.db import models
from django.db.models import Index
from django.utils.translation import gettext_lazy as _


class Dealer(User):
    city = models.ForeignKey(to='City', related_name='dealers', on_delete=models.CASCADE)

    class Meta:
        verbose_name = _('Dealer')
        verbose_name_plural = _('Dealer')

    @property
    def title(self):
        return f'{self.get_full_name()} from {self.city.name}, email: {self.email}'

    def __str__(self):
        return self.title


class City(models.Model):
    name = models.CharField(max_length=30)
    country = models.ForeignKey(to='Country', on_delete=models.SET_NULL, null=True, related_name='cities')

    class Meta:
        verbose_name = _('City')
        verbose_name_plural = _('Cities')

        indexes = [
            Index(fields=['name', ])
        ]

    def __str__(self):
        return self.name


class Country(models.Model):
    name = models.CharField(max_length=50, unique=True)
    code = models.IntegerField(null=True, blank=True, unique=True)

    class Meta:
        verbose_name = _('Country')
        verbose_name_plural = _('Countries')

        indexes = [
            Index(fields=['name', ])
        ]

    def __str__(self):
        return self.name
