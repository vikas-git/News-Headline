from django.shortcuts import render
from helpers.apiservice import get_api_data



# Create your views here.
def index(request):
    response = get_api_data('https://newsapi.org/v2/top-headlines', {'country': 'in'})
    print(response)
    return render(request, 'home/index.html', {})