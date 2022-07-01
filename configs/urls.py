from django.urls import path, include

urlpatterns = [
    path('cars', include('apps.cars.urls')),

]
# використовуємо include('apps.cars.urls') щоб не роздувати головну вюшку