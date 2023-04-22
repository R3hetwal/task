from django.contrib import admin
from django.urls import path
from api.viewsets.viewsets import get_data_for_Survey_publications, get_data_for_Survey_news, get_data_for_अन्य_उपयोगी_सामग्री, get_data_for_डाउनलोड_अन्य, get_data_for_डाउनलोड_ऐन_नियम, get_data_for_डाउनलोड_कार्यविधि, get_data_for_डाउनलोड_नियमावली, get_data_for_डाउनलोड_निर्देशिका, get_data_for_बारम्बार_सोधिने_प्रश्नहरु, get_data_for_सहकारी_सङ्घ_संस्था_तथ्याङ्क,  get_data_for_सूचनाको_हक, get_data_for_nlc_सूचना, get_data_for_nlc_डाउनलाेड

urlpatterns = [
    path('scrape-news', get_data_for_Survey_news),
    path('scrape-publications', get_data_for_Survey_publications),
    path('scrape-downloadsdetail/4/2017/17421968', get_data_for_अन्य_उपयोगी_सामग्री),
    path('scrape-downloadsdetail/5/2019/63273428', get_data_for_सूचनाको_हक),
    path('scrape-downloadsdetail/3/2017/76236913', get_data_for_सहकारी_सङ्घ_संस्था_तथ्याङ्क),
    path('scrape-office/dept/content/other-1659866558', get_data_for_डाउनलोड_अन्य),
    path('scrape-office/dept/content/rules-regulations', get_data_for_डाउनलोड_ऐन_नियम),
    path('scrape-office/dept/content/procedure-1635137665', get_data_for_डाउनलोड_कार्यविधि),
    path('scrape-office/dept/content/regulation-1635137640', get_data_for_डाउनलोड_नियमावली),
    path('scrape-office/dept/content/rules-1635137656', get_data_for_डाउनलोड_निर्देशिका),
    path('scrape-FAQ', get_data_for_बारम्बार_सोधिने_प्रश्नहरु),
    path('scrape-suchana', get_data_for_nlc_सूचना),
    path('scrape-download', get_data_for_nlc_डाउनलाेड),
]