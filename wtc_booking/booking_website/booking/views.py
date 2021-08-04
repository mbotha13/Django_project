from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Johannesburg_booking, Date, Month,Durban_booking,Cape_Town_booking
from django.core.mail import send_mail, EmailMessage
from django.conf import settings
from django.template.loader import render_to_string
from .forms import add_bookingForm, CapeBookingForm, DurbanBookingForm

# Create your views here.

def booking_page(request):
	submitted = False
	if request.method == "POST":
		form = add_bookingForm(request.POST)
		if form.is_valid():
			user_info = form.save(commit=False)
			user_info.user= request.user
			user_info.save()


			return HttpResponseRedirect('/add_booking?submitted=True')
	else:
		form = add_bookingForm
		if 'submitted' in request.GET:
			submitted = True
			template = render_to_string('booking_page/email_template.html',{'name':request.user.username})
			subject = 'WTC Bootcamp Booking Confirmation'
			message = f'Hello {request.user.username}, Your Booking has been confirmed'
			email_from = settings.EMAIL_HOST_USER
			recipient_list = [request.user.email,]
			send_mail( subject, message, email_from, recipient_list)
	return render(request, 'booking_page/add_booking.html', {'form':form, 'submitted':submitted})


def DurbanBookingPage(request):
	submitted = False
	if request.method == "POST":
		form = DurbanBookingForm(request.POST)
		if form.is_valid():
			user_info = form.save(commit=False)
			user_info.user= request.user
			user_info.save()


			return HttpResponseRedirect('/DurbanBooking?submitted=True')
	else:
		form = DurbanBookingForm
		if 'submitted' in request.GET:
			submitted = True
			template = render_to_string('booking_page/email_template.html',{'name':request.user.username})
			subject = 'WTC Bootcamp Booking Confirmation'
			message = f'Hello {request.user.username}, Your Booking has been confirmed'
			email_from = settings.EMAIL_HOST_USER
			recipient_list = [request.user.email,]
			send_mail( subject, message, email_from, recipient_list)
	return render(request, 'booking_page/add_booking.html', {'form':form, 'submitted':submitted})


def CapeBookingPage(request):
	submitted = False
	if request.method == "POST":
		form = CapeBookingForm(request.POST)
		if form.is_valid():
			user_info = form.save(commit=False)
			user_info.user= request.user
			user_info.save()


			return HttpResponseRedirect('/CapeBooking?submitted=True')
	else:
		form = CapeBookingForm
		if 'submitted' in request.GET:
			submitted = True
			template = render_to_string('booking_page/email_template.html',{'name':request.user.username})
			subject = 'WTC Bootcamp Booking Confirmation'
			message = f'Hello {request.user.username}, Your Booking has been confirmed'
			email_from = settings.EMAIL_HOST_USER
			recipient_list = [request.user.email,]
			send_mail( subject, message, email_from, recipient_list)

			# email = EmailMessage(
			# 	'WTC Bootcamp Booking Confirmation',
			# 	f'Hello {request.user.username}',
			# 	settings.EMAIL_HOST_USER,
			# 	[request.user.email],
			# )
			# email.send()

	return render(request, 'booking_page/add_booking.html', {'form':form, 'submitted':submitted})

def Send_email(request):
    submitted = False
    if 'submitted' in request.GET:
        submitted = True
        import booking.Email.mail
		# template = render_to_string('booking_page/email_template.html',{'name':request.user})
		# email = EmailMessage(
		# 		'WTC Bootcamp Booking Confirmation',
		# 		template,					settings.EMAIL_HOST_USER,
		# 		['bothamarc9@gmail.com'],