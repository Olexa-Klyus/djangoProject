from django.contrib import admin
from .models import CarModel


# Register your models here.
# admin.site.register(CarModel)

# або по своєму настроїти адмінку
@admin.register(CarModel)
class CarAdmin(admin.ModelAdmin):
    list_display = ('id', 'brand', 'price')
