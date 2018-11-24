from django.conf import settings
from django.utils.datastructures import MultiValueDict as MVD
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from profiles.models import Details
from django.core.mail import send_mail
from .models import user_payment
from Admins.models import RegAdmin

import stripe
 
stripe.api_key = settings.STRIPE_SECRET_KEY

@login_required
def checkout(request):
    publishKey = settings.STRIPE_PUBLISHABLE_KEY
    customer_id = request.user.userstripe.stripe_id

    x = Details.objects.get(user = request.user)

    if request.method == 'POST':
      stripe.Charge.create(
        amount=2000,
        currency="usd",
        source="tok_visa", # obtained with Stripe.js
        description="Charge for sofia.jones@example.com"
      )
      
      p = user_payment(user = request.user , applicant_number = str(x.aadhar_number)+'P'+str(x.pin_code)+'_A_'+x.city, 
                        payment = "successful")
      p.save()

      pin = x.pin_code

      x1 = RegAdmin.objects.get(pin_code = pin)
      email = x.email_id
      name = x.name
      comment = 'Reg Admin Name : '+x1.name+'\nApplicant Number : '+str(x.aadhar_number)+'P'+str(x.pin_code)+'_A_'+x.city+'\n'+'Name : '
      subject='New Passport Application '
      message = '%s %s' %(comment,name)
      emailFrom= email
      emailTo = [settings.EMAIL_HOST_USER]
      send_mail(subject,message,emailFrom,emailTo,fail_silently=False,)

      context = {}
      template = 'charge.html'
      return render(request,template,context)
        
    user = request.user
    context = {'publishKey':publishKey}
    template = 'checkout.html'
    return render(request,template,context)


def charge(request):
    
    context = {}
    template = 'charge.html'
    x = Details.object.get(user = request.user)
    email = x.email_id
    print (email)
    name = x.name
    comment = 'Applicant Number : '+x.aadhar_number+'P'+x.pin_code+'_A_'+x.city+'\n User Name : '+request.user
    subject='New Passport Application '
    message = '%s %s' %(comment,name)
    emailFrom= email
    emailTo = [settings.EMAIL_HOST_USER]
    send_mail(subject,message,emailFrom,emailTo,fail_silently=False,)
    return render(request,template,context)