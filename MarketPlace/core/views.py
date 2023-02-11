from django.shortcuts import render
from django.shortcuts import HttpResponse, redirect
from . import web_scraping4
from django.contrib import messages
from .web_scraping4 import compare 

# Create your views here.


def home(request):
     if request.method == 'POST':
       item = request.POST["Item"]
       price = request.POST["Price"]
       compare(item, price)
       
     return render(request, "index.html")

    



       


