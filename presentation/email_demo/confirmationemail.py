import smtplib, ssl
from smtplib import SMTPException

smtpServer = "smtp.gmail.com"
mySMTP = smtplib.SMTP("smtp.google.com") 
port = 587 
myEmail = "mbotha@student.wethinkcode.co.za"
password = "nowyourestudent" 
#email and password can also be user input fields
context = ssl.create_default_context()

emailSender = "mbotha@student.wethinkcode.co.za"
myThroaway = 'bothamarc9@gmail.com'
emailRecipients = [myThroaway]
newEmail = """From: From Person mbotha@student.wethinkcode.co.za
To: To Person bothamarc9@gmail.com
Subject: Email Test
This is the body of the email.
"""
try:
   smtpObj = smtplib.SMTP('smtp.gmail.com')
   mySMTP.sendmail(emailSender, emailRecipients, newEmail)
   print ("Email sent successfully!")
except SMTPException:
   print ("Error: There was an error in sending your email.")
mySMTP.sendmail(emailSender, emailRecipients, newEmail)
try:
    server = smtplib.SMTP(smtpServer,port)
    server.starttls(context=context)
    server.login(newEmail, password)
except Exception as e:
    print("the email could not be sent.")
finally:
    server.quit()
