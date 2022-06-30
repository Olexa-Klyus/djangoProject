from rest_framework.views import APIView
from rest_framework.response import Response

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
        return Response(serializer.data)

    def post(self, *args, **kwargs):
        data = self.request.data
        # instance = CarModel.objects.create(**data)
        # за допомогою серіалайзера перевіряємо валідність даних
        serializer = CarSerializer(data=data)
        if not serializer.is_valid():
            return Response(serializer.errors)
        serializer.save()
        return Response(serializer.data)


class CarUpdateRetrieveDestroyView(APIView):
    def get(self, *args, **kwargs):
        car_id = kwargs.get('pk')
        print(car_id)

        if not CarModel.objects.filter(pk=car_id).exists():
            return Response('Car is not found')

        car = CarModel.objects.get(pk=car_id)
        serializer = CarSerializer(car)
        return Response(serializer.data)

    def put(self, *args, **kwargs):
        data = self.request.data
        pk = kwargs.get('pk')

        if not CarModel.objects.filter(pk=pk).exists():
            return Response('Car is not found')

        car = CarModel.objects.get(pk=pk)
        serializer = CarSerializer(car, data)


        return Response(serializer.data)
