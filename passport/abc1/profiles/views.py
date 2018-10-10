from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.conf import settings

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

def regional_admin(request):
	context = {}
	template = 'regional_admin.html'
	return render(request,template,context)

@login_required
def userProfile(request):
	user = request.user
	context = {'user':user}
	template = 'profile.html'
	return render(request,template,context)