import csv
from rest_framework.decorators import api_view
from django.http import JsonResponse

@api_view(['GET'])
def get_data_for_department(request):
    department = request.GET.get('department', 'dos')
    content_type = request.GET.get('content_type', 'news')

    # Define a mapping from department and content type to CSV file names
    file_map = {
        ('dos', 'news'): 'scraped/scrape-news.csv',
        ('dos', 'publications'): 'scraped/Survey_publications.csv',
        ('deoc', 'downloadsdetail/4'): 'scraped/anyaupayogisamagri.csv',
        ('deoc', 'downloadsdetail/3'): 'scraped/sahakarisanghsansthatathyanka.csv',
        ('deoc', 'downloadsdetail/5'): 'scraped/suchanakohak.csv',
        ('dolma', 'other-1659866558'): 'scraped/downloadanya.csv',
        ('dolma', 'rules-regulations'): 'scraped/downloadyainniyam.csv',
        ('dolma', 'procedure-1635137665'): 'scraped/downloadkaryabidhi.csv',
        ('dolma', 'regulation-1635137640'): 'scraped/downloadniyamawali.csv',
        ('dolma', 'rules-1635137656'): 'scraped/downloadnirdeshika.csv',
        ('merokitta', 'faq'): 'scraped/faq.csv',
        ('nlc', 'notice'): 'scraped/nlcnotice.csv',
        ('nlc', 'downloads'): 'scraped/nlcdownloads.csv'
    }

    # Check if the requested department and content type are valid
    if (department, content_type) not in file_map:
        return JsonResponse({'error': 'Invalid department or content type. Missing "?department=xxx&content_type='},
                            {'content_type : news, publications for department : dos'},
                            {'content_type : downloadsdetail/4, downloadsdetail/3, downloadsdetail/5, for department : deoc'},
                            {'content_type : other-1659866558, rules-regulations, procedure-1635137665, regulation-1635137640, rules-1635137656 for department : dolma'},
                            {'content_type : faq, for department : merokitta'},
                            {'content_type : notice, downloads for department : nlc'},)

    # Scrape the data from the corresponding CSV file
    data = []
    with open(file_map[(department, content_type)]) as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)

    # Return the scraped data as a JSON response
    return JsonResponse(data, safe=False)

