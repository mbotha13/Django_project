from django.db import models

# Create your models here.
BOOTCAMP_CHOICES=(
		('LIVE','Live'),
		('REMOTE','Remote'),
	)



class Johannesburg_booking(models.Model):
	name = models.CharField('student name', max_length=55)
	email = models.EmailField('email', max_length=250)
	bootcamp_type = models.CharField('bootcamp_type',max_length=7,choices=BOOTCAMP_CHOICES,default='Live')
	bootcamp_month = models.CharField('bootcamp month',max_length=10)
	camp_date =models.CharField('bootcamp date', max_length=10)

	def __str__(self):
		return self.name

class Cape_Town_booking(models.Model):
	name = models.CharField('student name', max_length=55)
	email = models.EmailField('email', max_length=250)
	bootcamp_type = models.CharField('bootcamp_type',max_length=7,choices=BOOTCAMP_CHOICES,default='Live')
	bootcamp_month = models.CharField('bootcamp month',max_length=10)
	camp_date =models.CharField('bootcamp date', max_length=10)

	def __str__(self):
		return self.name

class Durban_booking(models.Model):
	name = models.CharField('student name', max_length=55)
	email = models.EmailField('email', max_length=250)
	bootcamp_type = models.CharField('bootcamp_type',max_length=7,choices=BOOTCAMP_CHOICES,default='Live')
	bootcamp_month = models.CharField('bootcamp month',max_length=10)
	camp_date =models.CharField('bootcamp date', max_length=10)

	def __str__(self):
		return self.name
