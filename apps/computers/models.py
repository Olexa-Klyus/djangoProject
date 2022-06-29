from django.db import models


# Создаем модель Computer
#
# поля:
# - бренд
# -модель
# - объем оперативной памяти
# - монитор (дюймы)
#
# реализовать все CRUD операции

class ComputerModel(models.Model):
    class Meta:
        db_table = 'computers'

    brand = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    ram = models.IntegerField()
    monitor = models.FloatField()
