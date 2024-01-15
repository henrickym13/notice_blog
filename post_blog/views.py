from django.shortcuts import render
from api.newsapi import NewsApi
from .models import Category
from requests.exceptions import SSLError

# Create your views here.
def home(request):
    try:
        if request.method == "GET":

            notices = NewsApi()
            notices = notices.api_request()

            category = Category.objects.get(name='brazil')

            return render(request, 'post_list.html', {'notices': notices, 'category': category})
        
    except SSLError:
        return render(request, 'error.html')


def theme_page(request, name):
    try:
        if request.method == "GET":

            notices = NewsApi()
            notices = notices.api_request_theme(name)

            category = Category.objects.get(name=name)

            return render(request, 'post_list.html', {'notices': notices, 'category': category})
        
    except SSLError:
        return render(request, 'error.html')
