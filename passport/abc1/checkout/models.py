from __future__ import unicode_literals
from django.db import models
from django.conf import settings
from allauth.account.signals import user_logged_in, user_signed_up
from django.contrib.auth.models import User
from django.utils.timezone import datetime
import stripe
 
stripe.api_key = settings.STRIPE_SECRET_KEY

class user_payment(models.Model):
	user = models.ForeignKey(User,on_delete=models.CASCADE,)
	payment = models.TextField(default = 'not paid')
	
	
	def __unicode__(self):
		return self.name
