from django.contrib.auth.models import User
from django.db import models
from django.db.models import Index
from django.utils.translation import gettext_lazy as _


class Dealer(User):
    Title = models.CharField(max_length=64)

    class Meta:
        verbose_name = _('Dealer')
        verbose_name_plural = _('Dealer')

    # def __str__(self):
    #     return self.name
