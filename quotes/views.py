from django.http import JsonResponse
from django.shortcuts import render
from django.forms.models import model_to_dict
from .models import Quote

# Create your views here.
def index(request):
    return render(request, 'quotes/index.html')

def quotes_json(request):
    quotes = Quote.objects.select_related('author').prefetch_related('categories')[:20]

    quote_list = []

    for quote in quotes:
        quote_dict = model_to_dict(quote, fields=['content'])
        quote_dict['author'] = quote.author.name
        quote_dict['category'] = [category.name for category in quote.categories.all()]

        quote_list.append(quote_dict)

    return JsonResponse(quote_list, safe=False)