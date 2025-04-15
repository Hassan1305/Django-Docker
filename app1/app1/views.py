import requests
from django.http import JsonResponse
from django.shortcuts import render

def call_app2(request):
    try:
        res = requests.get("http://app2:8000/thanks/")
        return JsonResponse({'response_from_app2': res.json()})
    except Exception as e:
        return JsonResponse({'error': str(e)})

def home(request):
    return render(request, 'home.html')
