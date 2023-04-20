from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'animate/index.html')

def spinner(request):
    return render(request, 'animate/spinner.html')