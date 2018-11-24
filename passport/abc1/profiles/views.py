from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.conf import settings
from .forms import DetailsForm,DocumentsForm
from .models import Details,Documents
from django.http import HttpResponse, HttpResponseRedirect
from checkout.models import user_payment
from django.core.files.storage import FileSystemStorage
from Admins.models import Dates,RegAdmin
from django.core.mail import send_mail

@login_required
def product_create_view(request):

	user = request.user

	if user_payment.objects.filter(user = user, payment = 'successful').exists() :
		context = {}
		template = 'redirect.html'
		return render(request,template,context)

	if Details.objects.filter(user = user).exists() :
		return HttpResponseRedirect('2')

	form = DetailsForm(request.POST or None)
	if form.is_valid():
		appl = form.save(commit = False)
		appl.user = request.user
		appl.save()
		return HttpResponseRedirect('2')

	context = {'form' : form}
	template = 'form1.html'
	return render(request,template,context)

def dashboard(request):

	k = -1
	q = -1

	if user_payment.objects.filter(user = request.user, payment = 'successful').exists() :
		data = Details.objects.get(user = request.user)
		data1 = user_payment.objects.get(user = request.user)

		if Dates.objects.filter(applicant_number = data1.applicant_number).exists():
			dates = Dates.objects.get(applicant_number = data1.applicant_number)
			context = {'data' : data,'dates':dates,'step':2}
			q = request.GET.get('date')
			x = Details.objects.get(user = request.user)
			x.date_of_appointment = q
			x.save()
			pin = x.pin_code
			x1 = RegAdmin.objects.get(pin_code = pin)
			email = x.email_id
			name = x.name
			comment = 'Reg Admin Name : '+x1.name+'\nApplicant Number : '+str(x.aadhar_number)+'P'+str(x.pin_code)+'_A_'+x.city+'\nDate of Appointment : '+str(q)+'\nName : '
			subject='New Passport Application '
			message = '%s %s' %(comment,name)
			emailFrom= email
			emailTo = [settings.EMAIL_HOST_USER]
			send_mail(subject,message,emailFrom,emailTo,fail_silently=True,)
			k = 0

		if k == 0:
			x = Details.objects.get(user = request.user)
			pin = x.pin_code
			x1 = RegAdmin.objects.get(pin_code = pin)
			context = {'data' : data,'date' : q,'step':3 , 'admin' : x1}
			
		else:
			context = {'data' : data,'step':1}
		template = 'dashboard.html'
		return render(request,template,context)


	else :
		context = {}
		template = 'redirect-1.html'
		return render(request,template,context)

@login_required
def documents_view(request):

	if Documents.objects.filter(user = request.user).exists() :
		return HttpResponseRedirect('payment')

	form = DocumentsForm(request.POST or None ,request.FILES or None)
	form.user = request.user
	if form.is_valid():
		cnt=-1;
		appl = form.save(commit = False)
		appl.user = request.user
		appl.save()
		return HttpResponseRedirect('payment')

	context = {
			'form' : form
		}
	template = 'user_form.html'

	return render(request,template,context)


def home(request):
	context = {}
	template = 'home.html'
	return render(request,template,context)

def about(request):
	context = {}
	template = 'about.html'
	return render(request,template,context)

def police(request):
	context = {}
	template = 'police.html'
	return render(request,template,context)

def admin_p(request):
	context = {}
	template = 'admin_p.html'
	return render(request,template,context)


@login_required
def userProfile(request):
	user = request.user
	context = {'user':user}
	template = 'profile.html'
	return render(request,template,context)