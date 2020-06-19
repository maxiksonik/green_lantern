from django.db import models
from django.db.models import Index
from django.utils.translation import gettext_lazy as _

from apps.cars.managers import CarManager, CarQuerySet
from common.models import BaseDateAuditModel
from djmoney.models.fields import MoneyField


class Color(models.Model):
    name = models.CharField(max_length=32, unique=True)

    class Meta:
        indexes = [
            Index(fields=('name',))
        ]

        verbose_name = _('Color')
        verbose_name_plural = _('Colors')

    def __str__(self):
        return self.name


class CarBrand(models.Model):
    name = models.CharField(max_length=32, unique=True)
    logo = models.ImageField(null=True, blank=False)

    class Meta:
        ordering = ('name',)
        indexes = [
            Index(fields=('name',))
        ]
        verbose_name = _('Car brand')
        verbose_name_plural = _('Car brands')

    def __str__(self):
        return self.name


class CarModel(models.Model):
    name = models.CharField(max_length=64)
    brand = models.ForeignKey(CarBrand, on_delete=models.CASCADE)

    class Meta:
        ordering = ('name',)
        indexes = [
            Index(fields=('name',)),
        ]
        verbose_name = _('Car model')
        verbose_name_plural = _('Car models')

    def __str__(self):
        return self.name


class Property(models.Model):
    name = models.CharField(max_length=25, blank=True)
    category = models.CharField(max_length=25, blank=True)
    car = models.ManyToManyField(to='cars.Car', related_name='property')


class Car(BaseDateAuditModel):
    STATUS_PENDING = 'pending'
    STATUS_PUBLISHED = 'published'
    STATUS_SOLD = 'sold'
    STATUS_ARCHIVED = 'archived'
    PETROL = 'PL'
    DIESEL = 'DL'
    GASEOUS = 'GS'
    HYBRID = 'HB'
    ELECTRIC = 'EC'
    TRANSMISSION_MANUAL = 'manual'
    TRANSMISSION_AUTOMATIC = 'automatic'

    STATUS_CHOICES = (
        (STATUS_PENDING, "Pending"),
        (STATUS_PUBLISHED, "Published"),
        (STATUS_SOLD, "Sold"),
        (STATUS_ARCHIVED, "Archived"),
    )

    ENGINE_TYPE_CHOICES = (
        (PETROL, 'Petrol engine'),
        (DIESEL, 'Diesel engine'),
        (GASEOUS, 'Gaseous engine'),
        (HYBRID, 'Hybrid engine'),
        (ELECTRIC, 'Electric engine'),
    )

    FUEL_TYPE_CHOICES = (
        (PETROL, 'Petrol'),
        (DIESEL, 'Diesel'),
        (GASEOUS, 'Gas'),
        (HYBRID, 'Hybrid'),
        (ELECTRIC, 'Electricity'),
    )

    GEAR_CASE_CHOICES = (
        (TRANSMISSION_MANUAL, 'Manual gear case'),
        (TRANSMISSION_AUTOMATIC, 'Automatic gear case'),
    )

    CURRENCY_CHOICES = (
        ('EUR', 'Euros'),
        ('USD', 'US Dollars'),
        ('UAH', 'Hryvnia')
    )

    objects = CarManager.from_queryset(CarQuerySet)()
    views = models.PositiveIntegerField(default=0, editable=False)
    slug = models.SlugField(max_length=75)
    number = models.CharField(max_length=16, unique=True)
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default=STATUS_PENDING, blank=True)
    dealer = models.ForeignKey(to='dealers.Dealer', on_delete=models.CASCADE, related_name='cars', null=True)

    model = models.ForeignKey(to='CarModel', on_delete=models.SET_NULL, null=True, related_name='cars')
    extra_title = models.CharField(max_length=255, null=True, blank=True, verbose_name=_('Title second part'))
    engine_type = models.CharField(max_length=2, choices=ENGINE_TYPE_CHOICES)
    fuel_type = models.CharField(max_length=2, choices=FUEL_TYPE_CHOICES)
    population_type = models.CharField(max_length=20, blank=True)
    price = MoneyField(currency_choices=CURRENCY_CHOICES, max_digits=10)
    doors = models.IntegerField(null=True, blank=True)
    engine_capacity = models.FloatField(null=True, blank=True)
    gear_case = models.CharField(max_length=9, choices=GEAR_CASE_CHOICES)
    sitting_place = models.IntegerField(null=True, blank=True)
    engine_power = models.IntegerField(null=True, blank=True)

    def save(self, *args, **kwargs):
        order_number_start = 7600000
        if not self.pk:
            super().save(*args, **kwargs)
            self.number = f"LK{order_number_start + self.pk}"
            self.save()
        else:
            super().save(*args, **kwargs)

    def delete(self, using=None, keep_parents=False):
        self.status = self.STATUS_ARCHIVED
        self.save()

    @property
    def title(self):
        return f'{self.model.brand} {self.extra_title or ""}'  # do not show None

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Car')
        verbose_name_plural = _('Cars')

        indexes = [
            Index(fields=['status', ])
        ]
