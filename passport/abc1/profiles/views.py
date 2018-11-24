from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.conf import settings
from .forms import DetailsForm,DocumentsForm
from .models import Details,Documents,profile
from django.http import HttpResponse, HttpResponseRedirect
from checkout.models import user_payment
from django.core.files.storage import FileSystemStorage
from police.models import pdb,cdb

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

	if user_payment.objects.filter(user = request.user, payment = 'successful').exists() :
		data = Details.objects.filter(user = request.user)
		context = {'data' : data}
		template = 'dashboard.html'
		return render(request,template,context)

	else :
		context = {}
		template = 'redirect-1.html'
		return render(request,template,context)

# @login_required
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

	if request.method == "POST":


		username = request.POST['username']
		password = request.POST['password']
		#print(username + password)

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
	id = request.POST.get('userid','')
	if user_payment.objects.filter(applicant_number= id).exists():
		obj = user_payment.objects.get(applicant_number = id)
		user = obj.user
		#print("step 1")
		if profile.objects.filter(user = user):
			base = profile.objects.get(user = user)
			name = base.name
			#print("step 2")
			if Details.objects.filter(name = name):
				#print("step 3")
				detobj = Details.objects.get(name = name)
				context={'detobj': detobj}
				return render(request,'details.html',context)
			else:
				context={}
				return render(request,'temp.html',context)
		else:
			context={}
			return render(request,'temp.html',context)
	else :
		print("wrong crdenilas")		
	context={}
	return render(request,'check.html',context)

def validate(request):
	adno = request.POST.get('adno','')
	if cdb.objects.filter(aadhaarcard=adno):
		context = {'data': "Applicant is a criminal hence not verified"}
		return render(request,'verify.html',context)
	else:
		obj = Details.objects.get(aadhar_number = adno)
		context={'data': "Applicant is not a criminal hence verified",'obj': obj}
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