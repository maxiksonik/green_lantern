from django.db import models
#from django.utils.translation import gettext_lazy as _
#from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.


class Order(models.Model):
    STATUS_PROCESSED = 'processed'
    STATUS_PENDING_PAYMENT = 'pending_payment'
    STATUS_PEID = 'paid'
    STATUS_ARCHIVED = 'archived'

    STATUS_CHOICES = (
        (STATUS_PROCESSED, "processed"),
        (STATUS_PENDING_PAYMENT, "pending_payment"),
        (STATUS_PEID, "paid"),
        (STATUS_ARCHIVED, "Archived"),
    )

    first_name = models.CharField(max_length=32, unique=True)
    last_name = models.CharField(max_length=32, unique=True)
    email = models.EmailField()
    #phone = PhoneNumberField(blank=True)
    message = models.TextField(max_length=500)
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default=STATUS_PROCESSED, blank=True)
    car = models.ManyToManyField(to='cars.Car')

    # class Meta:
    #     verbose_name = _('Order')
    #     verbose_name_plural = _('Orders')
    #
    #     indexes = [
    #         Index(fields=['last_name', 'phone'])
    #     ]