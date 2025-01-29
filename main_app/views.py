from django.shortcuts import render
from django.conf import settings
import os, json, requests

#
def home(request):
    
    if request.method == "POST":
        city_name = request.POST['city_name']
        api_key = settings.WEATHER_API_KEY
        url = 'https://api.weatherstack.com/current?access_key={}'.format(api_key)
        querystring = {"query":city_name}
        response= requests.get(url, params=querystring)
        response_data = response.json()
        
        # is respose empty
        return render(request, 'home.html', {'response_data': response_data})
        
    else:
        return render(request, 'home.html', {})

def about(request):
    
    return render(request, 'about.html', {})

def contact(request):
    
    return render(request, 'contact.html', {})