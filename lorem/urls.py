from django.urls import path
from . import views

app_name = 'lorem'

urlpatterns = [
    path('', views.index, { 'page_nr': None }, name='index'),
    path('page/<int:page_nr>', views.index, name='page'),
    path('page-text/<int:page_nr>', views.text, name='text')
]
