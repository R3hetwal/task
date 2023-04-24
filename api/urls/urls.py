from django.contrib import admin
from django.urls import path
from api.viewsets.viewsets import get_data_for_department

urlpatterns = [
    path('scrape-data', get_data_for_department, name='get_data_for_department'),
    path('scrape-data?scrape-data?department=dos&content_type=publications', get_data_for_department),
    path('scrape-data?scrape-data?department=dos&content_type=news', get_data_for_department),
    path('scrape-data?scrape-data?department=deoc&content_type=downloadsdetail/4', get_data_for_department),
    path('scrape-data?scrape-data?department=deoc&content_type=downloadsdetail/3', get_data_for_department),
    path('scrape-data?scrape-data?department=deoc&content_type=downloadsdetail/5', get_data_for_department),
    path('scrape-data?department=dolma&content_type=other-1659866558', get_data_for_department),
    path('scrape-data?department=dolma&content_type=procedure-1635137665', get_data_for_department),
    path('scrape-data?department=dolma&content_type=regulation-1635137640', get_data_for_department),
    path('scrape-data?department=dolma&content_type=rules-1635137656', get_data_for_department),
    path('scrape-data?department=dolma&content_type=rules-regulations', get_data_for_department),
    path('scrape-data?department=merokitta&content_type=faq', get_data_for_department),
    path('scrape-data?department=nlc&content_type=notice', get_data_for_department),
    path('scrape-data?department=nlc&content_type=downloads', get_data_for_department),
]
