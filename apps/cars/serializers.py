from rest_framework.serializers import ModelSerializer
from .models import CarModel


class CarSerializer(ModelSerializer):
    class Meta:
        model = CarModel
        # після привязки моделі визначаємо які поля будуть використовуватися в цьому serializers
        fields = ('id', 'brand', 'price', 'year')
        # або всі
        # fields = '__all__'
