from django.db import models


class OrderQuerySet(models.QuerySet):
    def published(self):
        return self.filter(status='processed')

    def pend_pay(self):
        return self.filter(status='pend_pay')

    def paid(self):
        return self.filter(status='paid')

    def archived(self):
        return self.filter(status='archived')


class OrderManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset()
