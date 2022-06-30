# from django.contrib import admin
from django.urls import path

from apps.cars.views import CarListCreateView, CarUpdateRetrieveDestroyView

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('cars', CarListCreateView.as_view()),
    path('cars/<int:pk>', CarUpdateRetrieveDestroyView.as_view()),

]
