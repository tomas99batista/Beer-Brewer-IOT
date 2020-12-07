from django.shortcuts import render
from .models import BeerValues

# Create your views here.


def index(request):
    all_beer_values = BeerValues.objects.all()
    last_beer_value = BeerValues.objects.latest('id')
    params = {'all_beer_values': all_beer_values,
              'last_beer_value': last_beer_value}
    return(request, 'dashboard.html', params)
