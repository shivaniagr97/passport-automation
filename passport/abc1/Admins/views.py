from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
from django.core.files.storage import FileSystemStorage
from checkout.models import user_payment
from .models import Dates,Appl,DocsVerified,VStatus
from django.contrib.auth.models import User
from .forms import DatesForm,ApplForm,StatusForm
from profiles.models import Documents


global_appnNo = 0


@login_required
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

	print("global variable = ")
	print(global_appnNo)
	#to get corresponding user object from user_payment table
	user1 = user_payment.objects.get(applicant_number = global_appnNo )
	#user3=user1.user
	user2 = User.objects.get(username = user1.user.username)
	#get the docs of that object
	docs = Documents.objects.get( user = user2 )
#	print(docs.aadhar_card.url )
#	print(docs.photo.url )
	
	form = StatusForm(request.POST or None)
	if form.is_valid():
		obj = form.save()
		p = DocsVerified(applicant_number = global_appnNo , verification_status = obj.verification_status)
   		p.save()
		# 
	context = {'docs': docs , 'form' : form }
	template = 'admin_verifyDocs.html'
	return render(request,template,context)
