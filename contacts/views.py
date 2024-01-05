from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from .models import Contacts

# Create your views here.

def contacts(request): # To handle submission
    if request.method == 'POST':
        listing_id = request.POST['listing_id']
        listing = request.POST['listing']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        realtor_email = request.POST['realtor_email']

        # Check if user has made inquery already (you can't prevent unregistred users from making multiple inquiries unless you add something like ip_tracking)
        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contacts.objects.all().filter(listing_id=listing_id, user_id=user_id)
            if has_contacted:
                messages.error(request, 'You have already made an inquiry for this listing')
                return redirect('/listings/'+listing_id)

        contacts = Contacts(listing=listing, listing_id=listing_id, name=name, email=email, phone=phone, message=message, user_id=user_id)

        contacts.save()

        # send mail
        send_mail(
            'Property Listing Inquiry', 
            'There has been an inquiry for ' + listing + '. Sign into admin panel for more info', 
            'chinemeremokpara93@gmail.com', 
            [realtor_email, 'chinemeremokpara93@gmail.com'], 
            fail_silently=False 
        )


        messages.success(request, 'Your request has been submitted, a realtor will get back to you soon')
        return redirect('/listings/'+listing_id)