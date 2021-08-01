from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
import csv
from .models import Johannesburg_booking
from .forms import add_bookingForm
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string

# Create your views here.
def home(request):
	submitted = False
	if request.method == "POST":
		# booking_form = Johannesburg_booking()
		form = add_bookingForm(request.POST)
		if form.is_valid():
<<<<<<< HEAD
			form.save()
			# booking_form.save()
=======
			user_info = form.save(commit=False)
			user_info.user= request.user
			user_info.save()


>>>>>>> origin/knkosi
			return HttpResponseRedirect('/add_booking?submitted=True')
	else:
		form = add_bookingForm
		if 'submitted' in request.GET:
			submitted = True
			import booking.Email.mail
			# template = render_to_string('booking_page/email_template.html')

			# email = EmailMessage(
			# 	'WTC Bootcamp Booking Confirmation',
			# 	template,
			# 	settings.EMAIL_HOST_USER,
			# 	['bothamarc9@gmail.com'],
			# )
			# email.fail_silently=False
			# email.send()
   
	return render(request, 'booking_page/add_booking.html', {'form':form, 'submitted':submitted})

# def export_csv(request):
#     response = HttpResponse(content_type = 'txt/csv')
    
#     writer = csv.writer(response)
#     writer.writerow(['username', 'email','type', 'date1', 'date2'])
#     for data in Johannesburg_booking.objects.all().values_list('name', 'email', 'bootcamp_type', 'bootcamp_month', 'camp_date'):
#         writer.writerow(data)
    
#     response['Content-Disposition'] = 'attachment; filename="detail.csv"'
    
#     return response