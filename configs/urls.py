# from django.contrib import admin
from django.urls import path

from cars.views import CarListCreateView

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('cars', CarListCreateView.as_view()),

]
