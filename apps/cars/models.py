from django.db import models
from django.core.validators import MaxLengthValidator, MinLengthValidator, MaxValueValidator, MinValueValidator


class CarModel(models.Model):
    class Meta:
        db_table = 'cars'

    # brand = models.CharField(max_length=100)
    # можна додати унікальність
    # brand = models.CharField(max_length=100, unique=True)

    # або дефолтне значення
    # brand = models.CharField(max_length=100, default='avto')
    # або дозволити порожнє поле, або щоб воно було null=True
    # brand = models.CharField(max_length=100, blank=True)

    # використати валідатори, імпортувавши їх попередньо
    # brand = models.CharField(max_length=100, blank=True, validators=(MinLengthValidator(5), MaxLengthValidator(25)))
    # year = models.IntegerField(validators=(MinValueValidator(2000),))
    # price = models.IntegerField(validators=(MaxValueValidator(50000),))
    # create_at = models.DateTimeField(auto_now_add=True)
    # update_at = models.DateTimeField(auto_now=True)

    brand = models.CharField(max_length=100)
    year = models.IntegerField()
    price = models.IntegerField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.brand
