from __future__ import unicode_literals
from django.db import models
from django.conf import settings
from allauth.account.signals import user_logged_in, user_signed_up
from django.contrib.auth.models import User
from django.utils.timezone import datetime
import stripe
 
stripe.api_key = settings.STRIPE_SECRET_KEY

# class policedatabase(models.Model):

# 	policename  = models.CharField(max_length = 120, null = True)
# 	pincode     = models.CharField(max_length = 6, null = True)
# 	post        = models.CharField(max_length = 20, null = True)
#     contact     = models.CharField(max_length = 20, null = True)
#     joiningdate = models.CharField(max_length = 20, null = True)

# 	def __unicode__(self):
# 		return self.policename

class pdb(models.Model):
	name = models.CharField(max_length = 120)
	pincode = models.CharField(max_length = 30)
	post = models.CharField(max_length = 20)
	contact = models.CharField(max_length = 20)
	joiningdate = models.DateField(max_length = 20)
	password = models.CharField(max_length = 20)


class cdb(models.Model):
	name = models.CharField(max_length = 120)
	reason = models.CharField(max_length=300)
	aadhaarcard = models.CharField(max_length=20)
	address = models.CharField(max_length = 100)
	doa = models.DateField(max_length=20)
	dor = models.DateField(max_length=20)
	
