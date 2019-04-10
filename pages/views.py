from django.shortcuts import render

from listings.models import Listing
from listings.choices import cities

listings = Listing.objects.order_by('-dated').filter(published=True)[:3]
# Create your views here.


def index(request):
    context={
        'listings': listings,
        'cities':cities,
    }
    return render(request,'pages/index.html', context)


def about(request):
    return render(request,'pages/about.html')