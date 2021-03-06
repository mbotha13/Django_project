import smtplib
import os
import passwords
import csv



with open('email.txt') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    student_data = list(csv_reader)
    # print(student_data)
        


EMAIL_ADRESS = os.environ.get('EMAIL_USER')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')


with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()
    
    smtp.login(EMAIL_ADRESS, EMAIL_PASSWORD)
    with open('email.txt') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            subject = 'Hello'
            body = f'Hello {row[0]}'
            
            msg = f'Subject: {subject}\n\n{body}'
            
            smtp.sendmail(EMAIL_ADRESS, f'{row[1]}', msg)