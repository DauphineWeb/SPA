from django.http import JsonResponse
from django.shortcuts import render
from django.forms.models import model_to_dict
from .models import Quote

# Create your views here.
def index(request):
    return render(request, 'quotes/index.html')

def quotes_json(request):
    return JsonResponse({ })