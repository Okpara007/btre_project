from django.shortcuts import render, get_object_or_404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .models import Listing
from .choices import bedroom_choices, price_choices, state_choices


# Create your views here.

def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)
     
    paginator = Paginator(listings, 3)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    context = {
        'listings': paged_listings
    }
    return render(request, 'listings/listings.html', context)

def listing(request, listing_id ): 
    listing = get_object_or_404(Listing, pk=listing_id)

    context = {
        'listing': listing
    }
    return render(request, 'listings/listing.html', context)

def search(request): 
    queryset_list = Listing.objects.order_by('-list_date')

    # keywords 
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords: # to make sure it isnt an empty string 
            queryset_list = queryset_list.filter(description__icontains=keywords) # search description for words typed into keyword box

    # city
    if 'city' in request.GET:
        city = request.GET['city']
        if city: # to make sure it isnt an empty string 
            queryset_list = queryset_list.filter(city__iexact=city) # to match the exact city, iexact(is case insensitive)

    # state
    if 'state' in request.GET:
        state = request.GET['state']
        if state: # to make sure it isnt an empty string 
            queryset_list = queryset_list.filter(state__iexact=state) # to match the exact state, iexact(is case insensitive)

    # bedrooms
    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms: # to make sure it isnt an empty string 
            queryset_list = queryset_list.filter(bedrooms__lte=bedrooms) # less than or equal to

    # price
    if 'price' in request.GET:
        price = request.GET['price']
        if price: # to make sure it isnt an empty string 
            queryset_list = queryset_list.filter(price__lte=price) # to match the exact price, iexact(is case insensitive)

    context = {
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
        'state_choices': state_choices, 
        'listings': queryset_list,
        'values': request.GET
    }
    return render(request, 'listings/search.html', context )

