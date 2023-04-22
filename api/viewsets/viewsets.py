import csv
from rest_framework.decorators import api_view
from django.http import JsonResponse

@api_view(['GET'])
def get_data_for_Survey_news(request):
    survey_name = request.GET.get('for')

    # Define a mapping from survey names to CSV file names
    survey_file_map = {
        'dos': 'scraped/scrape-news.csv',
    }

    # Check if the requested survey is valid
    if survey_name not in survey_file_map:
        return JsonResponse({'error': 'Invalid survey name. Missing "?for=parameters{dos}'})

    # Scrape the data from the corresponding CSV file
    data = []
    with open(survey_file_map[survey_name]) as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)

    # Return the scraped data as a JSON response
    return JsonResponse(data, safe=False)

@api_view(['GET'])
def get_data_for_Survey_publications(request):
    survey_name = request.GET.get('for')

    # Define a mapping from survey names to CSV file names
    survey_file_map = {
        'dos': 'scraped/Survey_publications.csv'
    }

    # Check if the requested survey is valid
    if survey_name not in survey_file_map:
        return JsonResponse({'error': 'Invalid survey name. Missing "?for=parameters{dos}'})

    # Scrape the data from the corresponding CSV file
    data = []
    with open(survey_file_map[survey_name]) as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)

    # Return the scraped data as a JSON response
    return JsonResponse(data, safe=False)

@api_view(['GET'])             
def get_data_for_अन्य_उपयोगी_सामग्री(request):
    survey_name = request.GET.get('for')

    # Define a mapping from survey names to CSV file names
    survey_file_map = {
        'deoc': 'scraped/anyaupayogisamagri.csv'
    }

    # Check if the requested survey is valid
    if survey_name not in survey_file_map:
        return JsonResponse({'error': 'Invalid survey name. '})

    # Scrape the data from the corresponding CSV file
    data = []
    with open(survey_file_map[survey_name]) as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)

    # Return the scraped data as a JSON response
    return JsonResponse(data, safe=False)


@api_view(['GET'])             
def get_data_for_डाउनलोड_अन्य(request):
    survey_name = request.GET.get('for')

    # Define a mapping from survey names to CSV file names
    survey_file_map = {
        'dolma': 'scraped/downloadanya.csv'
    }

    # Check if the requested survey is valid
    if survey_name not in survey_file_map:
        return JsonResponse({'error': 'Invalid survey name.'})

    # Scrape the data from the corresponding CSV file
    data = []
    with open(survey_file_map[survey_name]) as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)

    # Return the scraped data as a JSON response
    return JsonResponse(data, safe=False)

@api_view(['GET'])             
def get_data_for_डाउनलोड_ऐन_नियम(request):
    survey_name = request.GET.get('for')

    # Define a mapping from survey names to CSV file names
    survey_file_map = {
        'dolma': 'scraped/downloadyainniyam.csv'
    }

    # Check if the requested survey is valid
    if survey_name not in survey_file_map:
        return JsonResponse({'error': 'Invalid survey name.'})

    # Scrape the data from the corresponding CSV file
    data = []
    with open(survey_file_map[survey_name]) as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)

    # Return the scraped data as a JSON response
    return JsonResponse(data, safe=False)

@api_view(['GET'])             
def get_data_for_डाउनलोड_कार्यविधि(request):
    survey_name = request.GET.get('for')

    # Define a mapping from survey names to CSV file names
    survey_file_map = {
        'dolma': 'scraped/downloadkaryabidhi.csv'
    }

    # Check if the requested survey is valid
    if survey_name not in survey_file_map:
        return JsonResponse({'error': 'Invalid survey name.'})

    # Scrape the data from the corresponding CSV file
    data = []
    with open(survey_file_map[survey_name]) as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)

    # Return the scraped data as a JSON response
    return JsonResponse(data, safe=False)

@api_view(['GET'])                       
def get_data_for_डाउनलोड_नियमावली(request):
    survey_name = request.GET.get('for')

    # Define a mapping from survey names to CSV file names
    survey_file_map = {
        'dolma': 'scraped/downloadniyamawali.csv'
    }

    # Check if the requested survey is valid
    if survey_name not in survey_file_map:
        return JsonResponse({'error': 'Invalid survey name.'})

    # Scrape the data from the corresponding CSV file
    data = []
    with open(survey_file_map[survey_name]) as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)

    # Return the scraped data as a JSON response
    return JsonResponse(data, safe=False)

@api_view(['GET'])             
def get_data_for_डाउनलोड_निर्देशिका(request):
    survey_name = request.GET.get('for')

    # Define a mapping from survey names to CSV file names
    survey_file_map = {
        'dolma': 'scraped/downloadnirdeshika.csv'
    }

    # Check if the requested survey is valid
    if survey_name not in survey_file_map:
        return JsonResponse({'error': 'Invalid survey name.'})

    # Scrape the data from the corresponding CSV file
    data = []
    with open(survey_file_map[survey_name]) as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)

    # Return the scraped data as a JSON response
    return JsonResponse(data, safe=False)

@api_view(['GET'])             
def get_data_for_बारम्बार_सोधिने_प्रश्नहरु(request):
    survey_name = request.GET.get('for')

    # Define a mapping from survey names to CSV file names
    survey_file_map = {
        'merokitta': 'scraped/faq.csv'
    }

    # Check if the requested survey is valid
    if survey_name not in survey_file_map:
        return JsonResponse({'error': 'Invalid survey name.'})

    # Scrape the data from the corresponding CSV file
    data = []
    with open(survey_file_map[survey_name]) as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)

    # Return the scraped data as a JSON response
    return JsonResponse(data, safe=False)


@api_view(['GET'])             
def get_data_for_सहकारी_सङ्घ_संस्था_तथ्याङ्क(request):
    survey_name = request.GET.get('for')

    # Define a mapping from survey names to CSV file names
    survey_file_map = {
        'doec': 'scraped/sahakarisanghsansthatathyanka.csv'
    }

    # Check if the requested survey is valid
    if survey_name not in survey_file_map:
        return JsonResponse({'error': 'Invalid survey name.'})

    # Scrape the data from the corresponding CSV file
    data = []
    with open(survey_file_map[survey_name]) as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)

    # Return the scraped data as a JSON response
    return JsonResponse(data, safe=False)

# @api_view(['GET'])             
# def get_data_for_सूचना(request):
#     data = []
#     with open('scraped/suchana.csv') as file:
#         reader = csv.DictReader(file)
#         for row in reader:
#             data.append(row)
#     return JsonResponse(data, safe=False)

@api_view(['GET'])             
def get_data_for_सूचनाको_हक(request):
    survey_name = request.GET.get('for')

    # Define a mapping from survey names to CSV file names
    survey_file_map = {
        'doec': 'scraped/suchanakohak.csv'
    }

    # Check if the requested survey is valid
    if survey_name not in survey_file_map:
        return JsonResponse({'error': 'Invalid survey name.'})

    # Scrape the data from the corresponding CSV file
    data = []
    with open(survey_file_map[survey_name]) as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)

    # Return the scraped data as a JSON response
    return JsonResponse(data, safe=False)


@api_view(['GET'])             
def get_data_for_nlc_सूचना(request):
    survey_name = request.GET.get('for')

    # Define a mapping from survey names to CSV file names
    survey_file_map = {
        'doec': 'scraped/nlcnotice.csv'
    }

    # Check if the requested survey is valid
    if survey_name not in survey_file_map:
        return JsonResponse({'error': 'Invalid survey name.'})

    # Scrape the data from the corresponding CSV file
    data = []
    with open(survey_file_map[survey_name]) as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)

    # Return the scraped data as a JSON response
    return JsonResponse(data, safe=False)

@api_view(['GET'])             
def get_data_for_nlc_डाउनलाेड(request):
    survey_name = request.GET.get('for')

    # Define a mapping from survey names to CSV file names
    survey_file_map = {
        'doec': 'scraped/nlcdownloads.csv'
    }

    # Check if the requested survey is valid
    if survey_name not in survey_file_map:
        return JsonResponse({'error': 'Invalid survey name.'})

    # Scrape the data from the corresponding CSV file
    data = []
    with open(survey_file_map[survey_name]) as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)

    # Return the scraped data as a JSON response
    return JsonResponse(data, safe=False)
