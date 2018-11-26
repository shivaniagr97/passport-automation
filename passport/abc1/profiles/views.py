from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.conf import settings
from .forms import DetailsForm,DocumentsForm,StatusForm
from .models import Details,Documents,profile,Verified
from django.http import HttpResponse, HttpResponseRedirect
from django.utils.timezone import datetime
from checkout.models import user_payment
from django.core.files.storage import FileSystemStorage
from police.models import pdb,cdb
from Admins.models import Dates,RegAdmin
from Admins.models import Dates,RegAdmin,DocsVerified
from django.core.mail import send_mail


global_appnNo = 0
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
	police = 0
	if user_payment.objects.filter(user = request.user, payment = 'successful').exists() :
		data = Details.objects.get(user = request.user)
		data1 = user_payment.objects.get(user = request.user)

		x = Details.objects.get(user = request.user)
		pin = x.pin_code
		x1 = RegAdmin.objects.get(pin_code = pin)
		t = user_payment.objects.get(user = request.user)
		
		if Verified.objects.filter(applicant_number = t.applicant_number).exists() :
			y = Verified.objects.get(applicant_number = t.applicant_number)
			if y.verification_status == 'Yes' :
				context = {'data' : data,'step':5 }
			else:
				context = {'data' : data,'step':-5 }

		elif DocsVerified.objects.filter(applicant_number = t.applicant_number).exists() :
			y = DocsVerified.objects.get(applicant_number = t.applicant_number)
			print(y.verification_status)
			print(police)
			if y.verification_status == 'Yes' :
				context = {'data' : data,'step':4 , 'admin' : x1}
			else:
				context = {'data' : data,'step':-4 , 'admin' : x1}

		elif x.date_of_appointment is not None:
			context = {'data' : data,'date' : x.date_of_appointment,'step':3 , 'admin' : x1}

		elif Dates.objects.filter(applicant_number = data1.applicant_number).exists():
			dates = Dates.objects.get(applicant_number = data1.applicant_number)
			context = {'data' : data,'dates':dates,'step':2}
			q = request.GET.get('date')
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
			
			if x.date_of_appointment is not None:
				k = 0


			if k == 0:

				x = Details.objects.get(user = request.user)
				pin = x.pin_code
				x1 = RegAdmin.objects.get(pin_code = pin)
				context = {'data' : data,'date' : q,'step':3 , 'admin' : x1}

			if police == 1:
				print ("Police!!!")
			
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

	if request.method == "GET":
		username = request.GET.get('username')
		password = request.GET.get('password')
		
		if pdb.objects.filter(name = username).exists():
			#print("available")
			obj = pdb.objects.get(name = username)
			if obj.password == password:
				context = {}
				return render(request,'check.html',context)
			else:
				context={}
				return render(request,'temp.html',context)
		    	
		    	
		    				
		else:
			#print("not available")
			context={}
			return render(request,'police.html',context)

	context={}	
	return render(request,'police.html',context)        


def test(request):
	id = request.POST.get('userid')
	global global_appnNo
	global_appnNo = id
	if user_payment.objects.filter(applicant_number= id).exists():
		obj = user_payment.objects.get(applicant_number = id)
		user = obj.user
		print(user)

		if Details.objects.filter(user = user).exists():
				#print("step 3")
			detobj = Details.objects.get(user = user)
			context={'detobj': detobj}
			return render(request,'details.html',context)
		else:
			context={}
			return render(request,'temp.html',context)
		
	else :
		print("wrong crdentilas")		
	context={}
	return render(request,'check.html',context)

def validate(request):
	adno = request.POST.get('adno','')
	if cdb.objects.filter(aadhaarcard=adno):
		context = {'data': "Applicant is a criminal hence not verified. "}
		return render(request,'verify.html',context)
	else:
		form = StatusForm(request.POST or None)
		if form.is_valid():
			obj = form.save()
			p = Verified(applicant_number = global_appnNo , verification_status = obj.verification_status)
			p.save()
			return HttpResponseRedirect('/')
		# 
		obj = Details.objects.get(aadhar_number = adno)
		context={'data': "Applicant is not a criminal hence verified.",'obj': obj,'form':form}
		return render(request,'verify.html',context)
		context = {}
	return request(request,'details.html',context)					

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