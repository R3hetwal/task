import csv
from rest_framework.decorators import api_view
from django.http import JsonResponse

@api_view(['GET'])
def get_data_for_Survey_news(request):
    data = []
    with open('scraped/Survey_news.csv') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    return JsonResponse(data, safe=False)

@api_view(['GET'])             
def get_data_for_Survey_publications(request):
    data = []
    with open('scraped/Survey_publications.csv') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    return JsonResponse(data, safe=False)


@api_view(['GET'])             
def get_data_for_अन्य_उपयोगी_सामग्री(request):
    data = []
    with open('scraped/anyaupayogisamagri.csv') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    return JsonResponse(data, safe=False)


@api_view(['GET'])             
def get_data_for_डाउनलोड_अन्य(request):
    data = []
    with open('scraped/downloadanya.csv') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    return JsonResponse(data, safe=False)

@api_view(['GET'])             
def get_data_for_डाउनलोड_ऐन_नियम(request):
    data = []
    with open('scraped/downloadyainniyam.csv') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    return JsonResponse(data, safe=False)

@api_view(['GET'])             
def get_data_for_डाउनलोड_कार्यविधि(request):
    data = []
    with open('scraped/downloadkaryabidhi.csv') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    return JsonResponse(data, safe=False)

@api_view(['GET'])             
def get_data_for_डाउनलोड_नियमावली(request):
    data = []
    with open('scraped/downloadniyamawali.csv') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    return JsonResponse(data, safe=False)

@api_view(['GET'])             
def get_data_for_डाउनलोड_निर्देशिका(request):
    data = []
    with open('scraped/downloadnirdeshika.csv') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    return JsonResponse(data, safe=False)

@api_view(['GET'])             
def get_data_for_बारम्बार_सोधिने_प्रश्नहरु(request):
    data = []
    with open('scraped/faq.csv') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    return JsonResponse(data, safe=False)

@api_view(['GET'])             
def get_data_for_सहकारी_सङ्घ_संस्था_तथ्याङ्क(request):
    data = []
    with open('scraped/sahakarisanghsansthatathyanka.csv') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    return JsonResponse(data, safe=False)

@api_view(['GET'])             
def get_data_for_सूचना(request):
    data = []
    with open('scraped/suchana.csv') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    return JsonResponse(data, safe=False)

@api_view(['GET'])             
def get_data_for_सूचनाको_हक(request):
    data = []
    with open('scraped/suchanakohak.csv') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    return JsonResponse(data, safe=False)

@api_view(['GET'])             
def get_data_for_nlc_सूचना(request):
    data = []
    with open('scraped/nlcnotice.csv') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    return JsonResponse(data, safe=False)

@api_view(['GET'])             
def get_data_for_nlc_डाउनलाेड(request):
    data = []
    with open('scraped/nlcdownloads.csv') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    return JsonResponse(data, safe=False)