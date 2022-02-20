from http.client import HTTPResponse
from django.shortcuts import render
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string
from django.contrib import messages	
from django.shortcuts import redirect

# Create your views here.


def home_view(request):
    return render(request, "home/index.html", {})

def sendEmail(request):

	if request.method == 'POST':

		template = render_to_string('home/email_template.html', {
			'name':request.POST['name'],
			'email':request.POST['email'],
			'message':request.POST['message'],
			})

		email = EmailMessage(
			request.POST['subject'],
			template,
			settings.EMAIL_HOST_USER,
			['stepankolias0@gmail.com']
			)

		email.fail_silently=False
		email.send()
		messages.success(request, 'Message successfully send.')

	return redirect("/#contact")