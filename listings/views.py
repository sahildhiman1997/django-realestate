from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404
from .models import Listing
from listings.choices import cities

# Create your views here.


def index(request):
    listings = Listing.objects.order_by('-dated').filter(published=True)
    paginator = Paginator(listings, 4)
    page = request.GET.get('page')
    paged_listing = paginator.get_page(page)
    context = {
        'listings': paged_listing,
    }
    return render(request, 'listings/listings.html', context)


def search(request):
    queryset_list=Listing.objects.order_by('-dated')
    if 'keywords' in request.GET:
        keywords= request.GET['keywords']
        if keywords:
            queryset_list=queryset_list.filter(description__icontains=keywords)
    if 'city' in request.GET:
        city=request.GET['city']
        if city!='All Cities':
            queryset_list=queryset_list.filter(city__iexact=city)
    if 'city' in request.GET:
        city=request.GET['city']
        if city!='All Cities':
            queryset_list=queryset_list.filter(city__iexact=city)
    context={
        'cities':cities,
        'listings':queryset_list,
        'city':city,
        'keywords':keywords
    }
    return render(request, 'listings/search.html',context)


def listing(request, listing_id):
    listing= get_object_or_404(Listing, pk=listing_id)
    context={
        'listing':listing
    }
    return render(request, 'listings/listing.html',context)
