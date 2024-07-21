from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
import time
from .tasks import sendemail
import requests
import json
from django.core.cache import cache
from django.views.decorators.cache import cache_page
# Create your views here.
def indexView(request):
    return render(request, "index.html")

def send_email(request):
    sendemail.delay()
    return HttpResponse("aaaaaaaaaaa")

# def test(request):
#     # cache.delete("test_delay_api")
#     if cache.get("test_delay_api") is None:
#         response=requests.get("https://git.ir")
#         cache.set("test_delay_api",response,timeout=60  )    
#     return HttpResponse(cache.get("test_delay_api"))

@cache_page(60)
def test(request):
    response=requests.get("https://git.ir")    
    return HttpResponse(response)

# https://d6d22a6c-3cd5-4678-8d08-7892777ba0f0.mock.pstmn.io/test/delay/5/"
