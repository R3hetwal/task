from django.contrib import admin
from django.urls import path
from api.viewsets.viewsets import get_data_for_department

urlpatterns = [
    path('scrape-data', get_data_for_department, name='get_data_for_department'),
]
