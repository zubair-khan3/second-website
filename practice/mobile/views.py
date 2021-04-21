from django.http import HttpResponse
from django.shortcuts import render
import datetime


# Create your views here.
def mobile(request):
    num = {'num': '23'}
    return render(request, 'index.html', num)
