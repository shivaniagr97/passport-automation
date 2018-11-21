from django.conf import settings
from django.utils.datastructures import MultiValueDict as MVD
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
import stripe
 
stripe.api_key = settings.STRIPE_SECRET_KEY

@login_required
def checkout(request):
    publishKey = settings.STRIPE_PUBLISHABLE_KEY
    customer_id = request.user.userstripe.stripe_id

    if request.method == 'POST':
      stripe.Charge.create(
        amount=2000,
        currency="usd",
        source="tok_visa", # obtained with Stripe.js
        description="Charge for sofia.jones@example.com"
      )
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
    return render(request,template,context)