from django.db import models
from django.contrib.auth.models import User

# Create your models here.
BOOTCAMP_CHOICES=(
		('LIVE','Live'),
		('REMOTE','Remote'),
	)



class Johannesburg_booking(models.Model):
	user = models.ForeignKey(User, on_delete= models.CASCADE)
	email = models.ForeignKey(User,related_name= 'email', on_delete= models.CASCADE)
	bootcamp_type = models.CharField('bootcamp_type',max_length=7,choices=BOOTCAMP_CHOICES,default='Live')
	bootcamp_month = models.CharField('bootcamp month',max_length=10)
	camp_date =models.CharField('bootcamp date', max_length=10)

	def __str__(self):
		return self.user.username

class Cape_Town_booking(models.Model):
	name = models.CharField('student name', max_length=55)
	email = models.EmailField('email', max_length=250)
	bootcamp_type = models.CharField('bootcamp_type',max_length=7,choices=BOOTCAMP_CHOICES,default='Live')
	bootcamp_month = models.CharField('bootcamp month',max_length=10)
	camp_date =models.CharField('bootcamp date', max_length=10)

	def __str__(self):
		return self.name, self.email, self.bootcamp_month, self.bootcamp_type, self.camp_date

class Durban_booking(models.Model):
	name = models.CharField('student name', max_length=55)
	email = models.EmailField('email', max_length=250)
	bootcamp_type = models.CharField('bootcamp_type',max_length=7,choices=BOOTCAMP_CHOICES,default='Live')
	bootcamp_month = models.CharField('bootcamp month',max_length=10)
	camp_date =models.CharField('bootcamp date', max_length=10)

	def __str__(self):
		return self.name, self.email, self.bootcamp_month, self.bootcamp_type, self.camp_date
