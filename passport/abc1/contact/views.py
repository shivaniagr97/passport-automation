from django.shortcuts import render
from .forms import contactForms
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def contact(request):
	title = 'Contact'
	form = contactForms(request.POST or None)
	msg = None

	if form.is_valid():
		name = form.cleaned_data['name']
		comment = form.cleaned_data['comment']
		subject='Message from Mysite.com'
		message = '%s %s' %(comment,name)
		emailFrom=form.cleaned_data['email']
		emailTo = [settings.EMAIL_HOST_USER]
		send_mail(subject,message,emailFrom,emailTo,fail_silently=True,)
		title = 'Thanks'
		msg = 'We will get right back to you..'
		form = None

	context = {'title':title,'form':form,'msg':msg,}
	template = 'contact.html'
	return render(request,template,context)
