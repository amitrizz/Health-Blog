from django.http import HttpResponse
from django.shortcuts import render

def homePage(request):
    # return HttpResponse("Hello world")
    return render(request,'home.html')

