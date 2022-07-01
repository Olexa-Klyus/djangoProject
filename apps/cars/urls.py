from django.urls import path

from apps.cars.views import CarListCreateView, CarUpdateRetrieveDestroyView

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', CarListCreateView.as_view()),
    path('/<int:pk>', CarUpdateRetrieveDestroyView.as_view()),

]