from django.contrib import admin
from django.urls import path

from first.views import FirstView, SecondView, ThirdView, FourView,UsersView,UserByIdView

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('first', FirstView.as_view()),
    path('second', SecondView.as_view()),
    path('third/<str:name>/<int:age>', ThirdView.as_view()),
    path('four', FourView.as_view()),
    path('users', UsersView.as_view()),
    path('users/<int:id>', UserByIdView.as_view()),

]
