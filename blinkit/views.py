from django.shortcuts import render
from django.http import HttpResponse
def blinkit(request):
    return HttpResponse('my favourite food deliver app is blinkit')
