from rest_framework.views import APIView
from rest_framework.response import Response


class FirstView(APIView):
    def get(self, request):
        return Response('Method GET')

    def post(self, request):
        return Response('Method POST')

    def put(self, request):
        return Response('Method PUT')

    def patch(self, request):
        return Response('Method PATCH')

    def delete(self, request):
        return Response('Method DELETE')


# 2 варіант передачі параметрів через аргс

class SecondView(APIView):
    def get(self, *args, **kwargs):
        query_params = self.request.query_params.dict()
        print(query_params)
        return Response(query_params)


# 3 варіант передачі параметрів через кваркси
# в третьому варіанті якщо не дати параметрів, буде помилка

class ThirdView(APIView):
    def get(self, *args, **kwargs):
        print(kwargs)
        return Response(kwargs)


# 4 варіант передачі параметрів через боді

class FourView(APIView):
    def post(self, *args, **kwargs):
        data = self.request.data
        print(data)
        return Response(data)


users = [
    {'id': 1, 'name': 'Max1', 'age': 12},
    {'id': 2, 'name': 'Max2', 'age': 22},
    {'id': 3, 'name': 'Max3', 'age': 32},
    {'id': 4, 'name': 'Max4', 'age': 42},
]


class UsersView(APIView):
    def get(self, *args, **kwargs):
        return Response(users)


class UserByIdView(APIView):
    def get(self, *args, **kwargs):
        user_id = kwargs.get('id')
        return Response(users[user_id - 1])
