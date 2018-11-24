from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
from django.core.files.storage import FileSystemStorage
from checkout.models import user_payment
from .models import Dates,Appl,DocsVerified,VStatus,RegAdmin
from django.contrib.auth.models import User
from .forms import DatesForm,ApplForm,StatusForm,RegAdminForm
from profiles.models import Documents


global_appnNo = 0
global_AdminUser = 0

def admin_login(request):

	mail = request.GET.get('email_id')
	pswd = request.GET.get('password')

	if RegAdmin.objects.filter( email_id = mail).exists():
		useradmin = RegAdmin.objects.get( email_id = mail)
		if useradmin.password == pswd :
			global global_AdminUser
			global_AdminUser =  useradmin
			return HttpResponseRedirect('/admin_home/')


	context={}
	template = 'admin_login.html'
	return render(request,template,context)


def admin_home(request):
	context = {}
	template = 'admin_home.html'
	return render(request,template,context)


def dashboard(request):

	form = DatesForm(request.POST or None)
	if form.is_valid():
		form.save()


	context = {"form":form}
	template = 'admin_dash.html'
	return render(request,template,context)

def verify_app(request, *args, **kwargs):

	q = request.GET.get('applicant_number')
#	print("q =")#	print(q)
	if user_payment.objects.filter( applicant_number = q ).exists() :
		user = user_payment.objects.filter( applicant_number = q)
		global global_appnNo 
		global_appnNo = q
#		print("global var= ")
#		print(global_appnNo)
		return HttpResponseRedirect('2')

	context = {}
	template = 'admin_verifyAppn.html'
	return render(request,template,context)


def verify_docs(request):

	#to get corresponding user object from user_payment table
	user1 = user_payment.objects.get(applicant_number = global_appnNo )
	user2 = User.objects.get(username = user1.user.username)
	#get the docs of that object
	docs = Documents.objects.get( user = user2 )
	
	form = StatusForm(request.POST or None)
	if form.is_valid():
		obj = form.save()
		p = DocsVerified(applicant_number = global_appnNo , verification_status = obj.verification_status)
   		p.save()
   		return HttpResponseRedirect('/admin_home/')
		# 
	context = {'docs': docs , 'form' : form }
	template = 'admin_verifyDocs.html'
	return render(request,template,context)
