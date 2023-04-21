from django.contrib import admin
from django.urls import path, include
from api.viewsets.viewsets import get_data_for_Survey_publications, get_data_for_Survey_news, get_data_for_अन्य_उपयोगी_सामग्री, get_data_for_डाउनलोड_अन्य, get_data_for_डाउनलोड_ऐन_नियम, get_data_for_डाउनलोड_कार्यविधि, get_data_for_डाउनलोड_नियमावली, get_data_for_डाउनलोड_निर्देशिका, get_data_for_बारम्बार_सोधिने_प्रश्नहरु, get_data_for_सहकारी_सङ्घ_संस्था_तथ्याङ्क, get_data_for_सूचना, get_data_for_सूचनाको_हक, get_data_for_nlc_सूचना
from rest_framework import routers

urlpatterns = [
    path('dos/survey_news', get_data_for_Survey_news),
    path('dos/survey_publications', get_data_for_Survey_publications),
    path('deoc/downloadsdetail/4/2017/17421968/', get_data_for_अन्य_उपयोगी_सामग्री),
    path('deoc/downloadsdetail/5/2019/63273428/', get_data_for_सूचनाको_हक),
    path('deoc/common', get_data_for_सूचना),
    path('deoc/downloadsdetail/3/2017/76236913/', get_data_for_सहकारी_सङ्घ_संस्था_तथ्याङ्क),
    path('dolma//office/dept/content/other-1659866558', get_data_for_डाउनलोड_अन्य),
    path('dolma/office/dept/content/rules-regulations', get_data_for_डाउनलोड_ऐन_नियम),
    path('dolma//office/dept/content/procedure-1635137665', get_data_for_डाउनलोड_कार्यविधि),
    path('dolma/office/dept/content/regulation-1635137640', get_data_for_डाउनलोड_नियमावली),
    path('dolma/office/dept/content/rules-1635137656', get_data_for_डाउनलोड_निर्देशिका),
    path('merokitta/faq', get_data_for_बारम्बार_सोधिने_प्रश्नहरु),
    path('nlc/सूचना', get_data_for_nlc_सूचना),
]