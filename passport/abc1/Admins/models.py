from __future__ import unicode_literals
from django.db import models
from django.conf import settings
from allauth.account.signals import user_logged_in, user_signed_up
from django.contrib.auth.models import User
from django.utils.timezone import datetime


class RegAdmin(models.Model):
	
	name = models.CharField(max_length=100,null = True)
	address = models.CharField(max_length=100,null = True)
	city = models.CharField(max_length=100,null = True)
	state = models.CharField(max_length=100,null = True)
	pin_code = models.CharField(max_length=6,null = True)
	contact_number = models.CharField(max_length=20,null = True)
	email_id = models.EmailField()
	date_of_joining = models.DateField(null = True)

class Dates(models.Model):
	
	applicant_number = models.CharField(max_length = 120,null = True)
	from_date = models.DateField(default = datetime.today())
	to_date = models.DateField(default = datetime.today())


class Appl(models.Model):
	
	applicant_number = models.CharField(max_length = 120,null = True)
	

