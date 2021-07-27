import smtplib
import os
import booking.Email.passwords
import csv
from booking.models import Johannesburg_booking



# with open('email.txt') as csv_file:
#     csv_reader = csv.reader(csv_file, delimiter=',')
#     student_data = list(csv_reader)
    # print(student_data)
    
        


EMAIL_ADRESS = os.environ.get('EMAIL_USER')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')


with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()
    
    smtp.login(EMAIL_ADRESS, EMAIL_PASSWORD)
    name = Johannesburg_booking.name
    mail= Johannesburg_booking.email
    subject = 'Booking Confirmed'
    body = f'Hello {name}'
    
    msg = f'Subject: {subject}\n\n{body}'
    
    smtp.sendmail(EMAIL_ADRESS, 'bothamarc9@gmail.com', msg)