from django.db import models


class CarModel(models.Model):

    # щоб змінити назву таблиці при створенні командою pythun manage py migrate cars
    # потрібно створити клас Meta в класі
    class Meta:
        db_table = 'cars'

    brand = models.CharField(max_length=100)
    year = models.IntegerField()
    price = models.IntegerField()

