from django.db import models


class CarModel(models.Model):
    class Meta:
        db_table = 'cars'
        verbose_name = 'Car'

    brand = models.CharField(max_length=100)
    year = models.IntegerField()
    price = models.IntegerField()

    def __str__(self):
        return self.brand
