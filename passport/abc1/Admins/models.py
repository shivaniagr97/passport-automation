from __future__ import unicode_literals
from django.db import models
from django.conf import settings
from allauth.account.signals import user_logged_in, user_signed_up
from django.contrib.auth.models import User
from django.utils.timezone import datetime


class RegAdmin(models.Model):
	
	password = models.CharField(max_length=20,null = False,default=123)
	name = models.CharField(max_length=100,null = True)
	address = models.CharField(max_length=100,null = True)
	city = models.CharField(max_length=100,null = True)
	state = models.CharField(max_length=100,null = True)
	pin_code = models.CharField(max_length=6,null = True)
	contact_number = models.CharField(max_length=20,null = True)
	email_id = models.EmailField(null=False,default='reg1@gmail.com')
	date_of_joining = models.DateField(default = datetime.today())
	#user = models.ForeignKey(User,on_delete=models.CASCADE,default = 0 )

class Dates(models.Model):
	
	applicant_number = models.CharField(max_length = 120,null = True)
	from_date = models.DateField(default = datetime.today())
	to_date = models.DateField(default = datetime.today())


class Appl(models.Model):
	
	applicant_number = models.CharField(max_length = 120,null = True)

class VStatus(models.Model):
	
	VERIF_STATUS = (
		('Yes','Yes') , ('No','No'),
	)	
	verification_status = models.CharField(max_length=100, choices = VERIF_STATUS ,null = False, default = 'No')


class DocsVerified(models.Model):

	applicant_number = models.CharField(max_length = 120,null = True)

	VERIF_STATUS = (
		('Yes','Yes') , ('No','No'),
	)	
	verification_status = models.CharField(max_length=100, choices = VERIF_STATUS ,null = False, default = 'No')



