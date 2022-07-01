from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import CarModel
from .serializers import CarSerializer


# Create
# Read
# Update
# Delete

class CarListCreateView(APIView):
    def get(self, *args, **kwargs):
        qs = CarModel.objects.all()
        serializer = CarSerializer(instance=qs, many=True)
        return Response(serializer.data, status.HTTP_200_OK)

    def post(self, *args, **kwargs):
        data = self.request.data
        # instance = CarModel.objects.create(**data)

        # за допомогою серіалайзера перевіряємо валідність даних
        serializer = CarSerializer(data=data)
        if not serializer.is_valid():
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)


class CarUpdateRetrieveDestroyView(APIView):
    def get(self, *args, **kwargs):
        car_id = kwargs.get('pk')
        print(car_id)

        if not CarModel.objects.filter(pk=car_id).exists():
            return Response('Car is not found', status.HTTP_404_NOT_FOUND)

        car = CarModel.objects.get(pk=car_id)
        serializer = CarSerializer(car)
        return Response(serializer.data, status.HTTP_200_OK)

    def put(self, *args, **kwargs):
        data = self.request.data
        pk = kwargs.get('pk')

        if not CarModel.objects.filter(pk=pk).exists():
            return Response('Car is not found', status.HTTP_404_NOT_FOUND)

        # витягуємо з бази даних car
        car = CarModel.objects.get(pk=pk)
        # передаємо цей кар і те що прислав клієнт
        serializer = CarSerializer(car, data)

        # перевіряємо на валідність і пеовертаємо помилку якщо не валідне
        # if not serializer.is_valid():
        #     return Response(serializer.errors)

        # або є скорочений варіант запису цього
        serializer.is_valid(raise_exception=True)
        # зберігаємось в базу,(якщо не зробили перевірку, він не запише в базу)
        serializer.save()
        return Response(serializer.data,status.HTTP_200_OK)

    def patch(self, *args, **kwargs):
        # майже все як put
        data = self.request.data
        pk = kwargs.get('pk')

        if not CarModel.objects.filter(pk=pk).exists():
            return Response('Car is not found', status.HTTP_404_NOT_FOUND)

        car = CarModel.objects.get(pk=pk)
        # додаємо partial=True щоб не було помилки при довільній кількості полів
        serializer = CarSerializer(car, data, partial=True)

        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_200_OK)

    def delete(self, *args, **kwargs):
        pk = kwargs.get('pk')

        if not CarModel.objects.filter(pk=pk).exists():
            return Response('Car is not found', status.HTTP_404_NOT_FOUND)

        car = CarModel.objects.get(pk=pk)
        car.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
