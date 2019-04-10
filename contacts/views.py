from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Contact
from datetime import datetime
from django.core.mail import send_mail

# Create your views here.
def contact(request):
    if request.method == 'POST':
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        message=request.POST['message']
        user_id=request.POST['user_id']
        listing=request.POST['listing']
        listing_id=request.POST['listing_id']
        print ('hello rama')

        #check if enquiry has already been made
        if request.user.is_authenticated:
                user_id =request.user.id
                has_contacted=Contact.objects.all().filter(listing_id=listing_id,user_id=user_id)
                if has_contacted:
                        messages.error(request,'You have already made an enquiry for this listing')
                        return redirect('/listings/'+listing_id)

        contact=Contact(name=name,email=email,listing_id=listing_id,message=message,dated=datetime.now(),phone=phone,user_id=user_id,listing=listing)   
        contact.save()

     
        send_mail(
        f'Contacted related listing: {listing}',
        f'{message}',
        'sahildhiman1997@gmail.com',
        [email,'sahil@3sixtystreet.in'],
        fail_silently=False,
        )
        messages.success(request,' Your message was successfuly delivered')
        return redirect('/listings/'+listing_id)