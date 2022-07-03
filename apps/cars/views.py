from django.db.models import Q
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, CreateModelMixin, UpdateModelMixin, \
    DestroyModelMixin

from rest_framework.response import Response
from rest_framework import status

from .models import CarModel
from .serializers import CarSerializer


# class CarListCreateView(APIView):
#
#     def get(self, *args, **kwargs):
#         qs = CarModel.objects.all()
#         # формує строку запиту на всі карси з таблиці, які можна відфільтрувати перед власне самим виконанням запиту,
#         # тобто передаванням в серіалайзер
#         # qs = qs.filter(brand__in=('BMW', 'audi'))
#         # qs = qs.filter(brand__contains=('DI'))
#         # якщо потрібно ігнорити регістр
#         # qs = qs.filter(brand__icontains=('di'))
#
#         # аналогічно для числових
#         # qs = qs.filter(price__gt=2000)
#         # qs = qs.filter(price__range=(2000, 10000))
#         # qs = qs.filter(price__in=(6500, 10000))
#         # можна через Q записувати вирази
#         # qs = qs.filter(Q(price__in=(6500, 10000)) | Q(brand__contains=('DI')))
#
#         # а також можна переда один елемент, але тоді забрати many з серіалайзера
#         # qs = qs.filter(price__gt=1000).last()
#         # serializer = CarSerializer(instance=qs)
#
#         # Можна порахувати і вивести в консоль
#         # qs = qs.filter(price__gt=1000)
#         # print(qs.count())
#
#         # з сортуванням, по декількох полях, від більшого до меншого
#         # qs = qs.filter(price__gt=1000).order_by('price', '-year')
#
#         # розвернути і взяти зріз з другого до четвертого, можна також додати крок,
#         # але тоді запит буде не просто сформований, а  відразу буде виконаний
#         # qs = qs.filter(price__gt=1000).order_by('price', '-year').reverse()[2:4]
#         # є ще можливість щось виключити -
#         # qs = qs.filter(price__gt=1000).order_by('price', '-year').reverse().exclude(brand='BMW')
#
#         # дані для фільтрації можна передати через query_params
#         # якщо він буде, виконається фільтр
#         price_gt = self.request.query_params.get('price_gt')
#
#         if price_gt:
#             qs = qs.filter(price__gt=price_gt)
#
#         serializer = CarSerializer(instance=qs, many=True)
#
#         return Response(serializer.data, status.HTTP_200_OK)
#
#     def post(self, *args, **kwargs):
#         data = self.request.data
#         # instance = CarModel.objects.create(**data)
#
#         # за допомогою серіалайзера перевіряємо валідність даних
#         serializer = CarSerializer(data=data)
#         if not serializer.is_valid():
#             return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
#
#         serializer.save()
#         return Response(serializer.data, status.HTTP_201_CREATED)
#
#
# class CarUpdateRetrieveDestroyView(APIView):
#     queryset = CarModel.objects.all()
#     serializer_class = CarSerializer
#
#     def get(self, *args, **kwargs):
#         car_id = kwargs.get('pk')
#
#         if not CarModel.objects.filter(pk=car_id).exists():
#             return Response('Car is not found', status.HTTP_404_NOT_FOUND)
#
#         car = CarModel.objects.get(pk=car_id)
#
#         serializer = CarSerializer(car)
#         return Response(serializer.data, status.HTTP_200_OK)
#
#     def put(self, *args, **kwargs):
#         data = self.request.data
#         pk = kwargs.get('pk')
#
#         if not CarModel.objects.filter(pk=pk).exists():
#             return Response('Car is not found', status.HTTP_404_NOT_FOUND)
#
#         # витягуємо з бази даних car
#         car = CarModel.objects.get(pk=pk)
#         # передаємо цей кар і те що прислав клієнт
#         serializer = CarSerializer(car, data)
#
#         # перевіряємо на валідність і пеовертаємо помилку якщо не валідне
#         # if not serializer.is_valid():
#         #     return Response(serializer.errors)
#
#         # або є скорочений варіант запису цього
#         serializer.is_valid(raise_exception=True)
#         # зберігаємось в базу,(якщо не зробили перевірку, він не запише в базу)
#         serializer.save()
#         return Response(serializer.data, status.HTTP_200_OK)
#
#     def patch(self, *args, **kwargs):
#         # майже все як put
#         data = self.request.data
#         pk = kwargs.get('pk')
#
#         if not CarModel.objects.filter(pk=pk).exists():
#             return Response('Car is not found', status.HTTP_404_NOT_FOUND)
#
#         car = CarModel.objects.get(pk=pk)
#         # додаємо partial=True щоб не було помилки при довільній кількості полів
#         serializer = CarSerializer(car, data, partial=True)
#
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status.HTTP_200_OK)
#
#     def delete(self, *args, **kwargs):
#         pk = kwargs.get('pk')
#
#         if not CarModel.objects.filter(pk=pk).exists():
#             return Response('Car is not found', status.HTTP_404_NOT_FOUND)
#
#         car = CarModel.objects.get(pk=pk)
#         car.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

#
#
# # запис через GenericAPIView
# class CarListCreateView(GenericAPIView):
#     queryset = CarModel.objects.all()
#     serializer_class = CarSerializer
#
#     def get(self, *args, **kwargs):
#         qs = self.get_queryset()
#
#         # серіалайзер вмикаємо через self.serializer_class
#         serializer = self.serializer_class(qs, many=True)
#         return Response(serializer.data, status.HTTP_200_OK)
#
#     def post(self, *args, **kwargs):
#         data = self.request.data
#         # instance = CarModel.objects.create(**data)
#
#         # за допомогою серіалайзера перевіряємо валідність даних
#         serializer = CarSerializer(data=data)
#         if not serializer.is_valid():
#             return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
#
#         serializer.save()
#         return Response(serializer.data, status.HTTP_201_CREATED)
#
#
# class CarUpdateRetrieveDestroyView(GenericAPIView):
#     queryset = CarModel.objects.all()
#     serializer_class = CarSerializer
#
#     def get(self, *args, **kwargs):
#
#         # в Generic serializer є self.get_object()
#         car = self.get_object()
#         serializer = self.serializer_class(car)
#         return Response(serializer.data, status.HTTP_200_OK)
#
#     def put(self, *args, **kwargs):
#         data = self.request.data
#         pk = kwargs.get('pk')
#
#         if not CarModel.objects.filter(pk=pk).exists():
#             return Response('Car is not found', status.HTTP_404_NOT_FOUND)
#
#         # витягуємо з бази даних car
#         car = CarModel.objects.get(pk=pk)
#         # передаємо цей кар і те що прислав клієнт
#         serializer = CarSerializer(car, data)
#
#         # перевіряємо на валідність і пеовертаємо помилку якщо не валідне
#         # if not serializer.is_valid():
#         #     return Response(serializer.errors)
#
#         # або є скорочений варіант запису цього
#         serializer.is_valid(raise_exception=True)
#         # зберігаємось в базу,(якщо не зробили перевірку, він не запише в базу)
#         serializer.save()
#         return Response(serializer.data, status.HTTP_200_OK)
#
#     def patch(self, *args, **kwargs):
#         # майже все як put
#         data = self.request.data
#         pk = kwargs.get('pk')
#
#         if not CarModel.objects.filter(pk=pk).exists():
#             return Response('Car is not found', status.HTTP_404_NOT_FOUND)
#
#         car = CarModel.objects.get(pk=pk)
#         # додаємо partial=True щоб не було помилки при довільній кількості полів
#         serializer = CarSerializer(car, data, partial=True)
#
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status.HTTP_200_OK)
#
#     def delete(self, *args, **kwargs):
#         pk = kwargs.get('pk')
#
#         if not CarModel.objects.filter(pk=pk).exists():
#             return Response('Car is not found', status.HTTP_404_NOT_FOUND)
#
#         car = CarModel.objects.get(pk=pk)
#         car.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


#
#
# # запис через Mixing
# class CarListCreateView(GenericAPIView, CreateModelMixin, ListModelMixin):
#     queryset = CarModel.objects.all()
#     serializer_class = CarSerializer
#
#     # a фільтр реалізуємо через додатковий метод, який змінює реквест
#     def get_queryset(self):
#         price_gt = self.request.query_params.get('price_gt')
#         if price_gt:
#             self.queryset.filter(price__gt=price_gt)
#         return super().get_queryset()
#
#     def get(self, *args, **kwargs):
#         return super().list(self.request, *args, **kwargs)
#
#     def post(self, *args, **kwargs):
#         return super().create(self.request, *args, **kwargs)
#
#
# class CarUpdateRetrieveDestroyView(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
#     queryset = CarModel.objects.all()
#     serializer_class = CarSerializer
#
#     def get(self, *args, **kwargs):
#         return super().retrieve(self.request, *args, **kwargs)
#
#     def put(self, *args, **kwargs):
#         return super().update(self.request, *args, **kwargs)
#
#     def patch(self, *args, **kwargs):
#         return super().partial_update(self.request, *args, **kwargs)
#
#     def delete(self, *args, **kwargs):
#         return super().destroy(self.request, *args, **kwargs)
#
#

# запис через об'єднані з GenericAPIView класи дуже компактно
class CarListCreateView(ListCreateAPIView):
    queryset = CarModel.objects.all()
    serializer_class = CarSerializer

    # a фільтр реалізуємо через додатковий метод, який змінює реквест
    def get_queryset(self):
        price_gt = self.request.query_params.get('price_gt')
        if price_gt:
            self.queryset.filter(price__gt=price_gt)
        return super().get_queryset()


class CarUpdateRetrieveDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = CarModel.objects.all()
    serializer_class = CarSerializer
