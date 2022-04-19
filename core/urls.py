from django.urls import path
from .views import index, pag1

urlpatterns = [
    path('', index, name="index"),
    path('pag1', pag1, name="pag1"),
]