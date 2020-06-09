from django.db import models
from common.models import BaseDateAuditModel
from django.utils.translation import gettext_lazy as _


class Newsletter(BaseDateAuditModel):
    email = models.EmailField()

    class Meta:
        verbose_name = _('Newsletter')
        verbose_name_plural = _('Newsletters')

    def __str__(self):
        return self.email
