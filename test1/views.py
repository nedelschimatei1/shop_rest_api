from django.shortcuts import render
from django.core.cache import cache
from django.core.mail import send_mail, BadHeaderError
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework.views import APIView
import requests
from .tasks import notify_customers
# Create your views here.


# @cache_page(5*60)
# def hello_test(request):
#     # key = 'httpbin_res'
#     # if cache.get(key) is None:
#     response = requests.get('https://httpbin.org/delay/3')
#     data = response.json()
#     # cache.set(key, data)
#     return render(request, 'test.html', {'test': data})

class HelloView(APIView):
    @method_decorator(cache_page(5*60))
    def get(self, request):
        response = requests.get('https://httpbin.org/delay/3')
        data = response.json()
        return render(request, 'test.html', {'test': data})
