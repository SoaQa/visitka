from django.urls import path
from .views import index, hello

app_name = 'main'

urlpatterns = [path('', index, name="index"),
               path('/hello', hello)]
