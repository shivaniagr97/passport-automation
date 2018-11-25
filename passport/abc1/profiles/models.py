from __future__ import unicode_literals
from django.db import models
from django.conf import settings
from allauth.account.signals import user_logged_in, user_signed_up
from django.contrib.auth.models import User
from django.utils.timezone import datetime
from django.core.validators import FileExtensionValidator
import stripe
 
stripe.api_key = settings.STRIPE_SECRET_KEY

class profile(models.Model):
	name = models.CharField(max_length = 120)
	user = models.OneToOneField(settings.AUTH_USER_MODEL,null=True,blank=True,on_delete=models.CASCADE)
	description = models.TextField(default = 'description default text')
	
	
	def __unicode__(self):
		return self.name


class userStripe(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
	stripe_id = models.CharField(max_length = 200,null=True,blank = True )

	def __unicode__(self):
		if self.stripe_id :
			return self.stripe_id
		else:
			return self.user.username


class Details(models.Model):
	GENDER_CHOICES = (
		('Male','M'),('Female','F'),('Transgender','Trans'),
	)

	MARITAL_STATUS_CHOICE = (
		('Single','Single'),('Married','Married'),('Divorced','Divorced'),('Widow/Widower','Widow/Widower'),('Separated','Separated'),
	)

	EMPLOYEMENT_STATUS_CHOICES = (
		('PSU','PSU'),('Government','Government'),('Retired Government Servant','Retired Government Servant'),('Self Employed','Self Employed'),('NOt Employed','Not Employed'),('Homemaker','Homemaker'),('Private','Private'),('Student','Student'),('Others','Others'),
	)

	EDUCATIONAL_QUALIFICATION_CHOICES = (
		('7th pass or less','7th pass or less'),('Between 8th and 9th Standard','Between 8th and 9th Standard'),('10th pass and above','10th pass and above'),('Graduate and above','Graduate and above'),
	)
	name = models.CharField(max_length=200,null = True)

	house_no = models.CharField(max_length=20,null = True)
	colony_or_location = models.CharField(max_length=100,null = True)
	city = models.CharField(max_length=100,null = True)
	district = models.CharField(max_length=100,null = True)
	state = models.CharField(max_length=100,null = True)
	pin_code = models.CharField(max_length=6,null = True)
	contact_number = models.CharField(max_length=20,null = True)
	emergency_contact_number = models.CharField(max_length=20,null = True)
	email_id = models.EmailField()


	gender = models.CharField(max_length=100, choices = GENDER_CHOICES,null = True)

	marital_status = models.CharField(max_length = 100, choices = MARITAL_STATUS_CHOICE,null = True)

	date_of_birth = models.DateField(null = True)
	birth_place = models.CharField(max_length=500,null=True)

	employement_status = models.CharField(max_length=100, choices = EMPLOYEMENT_STATUS_CHOICES,null = True)
	pan = models.CharField(max_length=10,null = True)
	voter_id = models.CharField(max_length=16,null = True)
	aadhar_number = models.CharField(max_length=12,null=True)

	father_name = models.CharField(max_length=200,null = True)
	mother_name = models.CharField(max_length=200,null = True)
	guardian_name = models.CharField(max_length=200,null = True)
	spouse_name = models.CharField(max_length=200,null = True)

	educational_qualification = models.CharField(max_length=100, choices = EDUCATIONAL_QUALIFICATION_CHOICES,null=True)

	user = models.ForeignKey(User,on_delete=models.CASCADE,)
	date_of_appointment = models.DateField(null = True)

	def __unicode__(self):
		return "PAS"+self.pin_code+"A"+self.aadhar_number

class Documents(models.Model):
	aadhar_card = models.FileField(null = True,upload_to = 'Documents/%Y/%m/%d/',validators=[FileExtensionValidator(allowed_extensions=['pdf'])])
	address_proof = models.FileField(null = True,upload_to = 'Documents/%Y/%m/%d/',validators=[FileExtensionValidator(allowed_extensions=['pdf'])])
	birth_certificate_or_matric_marksheet = models.FileField(null = True,upload_to = 'Documents/%Y/%m/%d/',validators=[FileExtensionValidator(allowed_extensions=['pdf'])])
	photo = models.ImageField(upload_to = 'Documents/%Y/%m/%d/',null = True)
	birth_certificate_or_matric_marksheet = models.FileField(upload_to = 'Documents/%Y/%m/%d/',validators=[FileExtensionValidator(allowed_extensions=['pdf'])],null = True)
	user = models.ForeignKey(User,on_delete=models.CASCADE,)

def stripeCallback(sender, request, user, **kwargs):
	#when user is logged in also want the model to create a profile for it
	user_stripe_account , created = userStripe.objects.get_or_create(user=user)
	if created:
		print('created for user %s'%(user.username))
	if user_stripe_account.stripe_id == None or user_stripe_account.stripe_id == '':
		new_stripe_id = stripe.Customer.create(email=user.email)
		user_stripe_account.stripe_id = new_stripe_id['id']
		user_stripe_account.save()


def profileCallback(sender, request, user, **kwargs):
	#when user is logged in also want the model to create a profile for it
	userProfile, is_created = profile.objects.get_or_create(user=user)
	if is_created:
		userProfile.name = user.username
		userProfile.save()


user_logged_in.connect(stripeCallback)
user_signed_up.connect(profileCallback)