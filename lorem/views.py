from django.shortcuts import render, HttpResponse
from django.http import Http404

def index(request):
    return render(request, 'lorem/index.html')
