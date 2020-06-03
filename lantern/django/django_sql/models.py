from django.db import models
from django.db.models import Index


class City(models.Model):
    city_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    country = models.ForeignKey('Country', on_delete=models.DO_NOTHING, blank=True, db_constraint=False)


class Country(models.Model):
    country_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)


class Dish(models.Model):
    dish_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    menu_id = models.IntegerField()
    price = models.FloatField()


class Menu(models.Model):
    menu_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=6)
    restaurant = models.ForeignKey('Restaurant', on_delete=models.DO_NOTHING, blank=True, db_constraint=False)
    dishes = models.ManyToManyField(Dish)


class Restaurant(models.Model):
    restaurant_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50, blank=True, null=True)
    city = models.ForeignKey('City', on_delete=models.DO_NOTHING, blank=True, db_constraint=False)


class Staff(models.Model):
    staff_id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    age = models.IntegerField(blank=True, null=True)
    address = models.CharField(max_length=50, blank=True, null=True)
    salary = models.FloatField()
    phone_number = models.CharField(max_length=13, blank=True, null=True)
    restaurant = models.ForeignKey('Restaurant', on_delete=models.DO_NOTHING, db_constraint=False)

    class Meta:
        indexes = [
            Index(fields=('first_name',))
        ]
