from django.shortcuts import render
import requests
from django.http import JsonResponse


def product_data(request):
    response = requests.get('https://fakestoreapi.com/products')
    data = response.json()
    return JsonResponse(data, safe=False)


# error handling
def product_data(request):
    try:
        response = requests.get('https://fakestoreapi.com/products')
        response.raise_for_status()
        data = response.json()
        return JsonResponse(data, safe=False)
    except requests.exceptions.RequestException as e:
        return JsonResponse({'error': str(e)}, status=500)
    

def home(request):
    return render(request, 'home.html')