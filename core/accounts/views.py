from django.shortcuts import render
from django.http import HttpResponse
import time
from .tasks import sendEmail
# Create your views here.
def send_email(request):
    j=sendEmail.delay()
    return HttpResponse(f"<h1>{j} Done Sending</h1>")