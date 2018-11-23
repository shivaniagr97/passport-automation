from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
from django.core.files.storage import FileSystemStorage
from checkout.models import user_payment
from .models import Dates,Appl
from .forms import DatesForm,ApplForm

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
	print(q)
	context = {}
	template = 'admin_verifyAppn.html'
	return render(request,template,context)
