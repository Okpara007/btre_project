from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Listing
from listings.choices import bedroom_choices, price_choices, state_choices
from realtors.models import Realtor

# Create your views here.
def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]
    context = { # pass the choices importation into the index.html through the context
        'listings': listings,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
        'state_choices': state_choices 
    }
    return render(request,"pages/index.html", context) # this enables us to convert the static home page to be dynamic

def about(request):
    # Get all realtors
    realtors = Realtor.objects.order_by('-hire_date')
    # Get MVP
    mvp_realtors = Realtor.objects.all().filter(is_mvp=True)

    context = {
        'realtors': realtors,
        'mvp_realtors': mvp_realtors
    }
    return render(request, "pages/about.html", context) 


