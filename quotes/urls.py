from django.urls import path
from . import views

app_name = 'quotes'

urlpatterns = [
    path('', views.index, name='index'),
    path('fetch-quotes/', views.quotes_json, name='fetch_quotes')
]
