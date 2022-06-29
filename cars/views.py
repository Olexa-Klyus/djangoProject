from rest_framework.views import APIView
from rest_framework.response import Response

from .models import CarModel


class CarListCreateView(APIView):

    def get(self, *args, **kwargs):
        return Response()


    def post(self, *args, **kwargs):
        data = self.request.data
        instance = CarModel.objects.create(**data)
        return Response('created')
