from django.db import models
from django.contrib.auth.models import User

# Create your models here.
BOOTCAMP_CHOICES=(
		('LIVE','Live'),
		('REMOTE','Remote'),
	)

class Month(models.Model):
	name = models.CharField(max_length=30)

	def __str__(self):
		return self.name

class Date(models.Model):
	month = models.ForeignKey(Month, on_delete = models.CASCADE)
	name = models.CharField(max_length = 10)

	def __str__(self):
		return self.month.name + '	'+  self.name 

class Johannesburg_booking(models.Model):
	user = models.ForeignKey(User, on_delete= models.CASCADE)
	bootcamp_type = models.CharField('bootcamp_type',max_length=7,choices=BOOTCAMP_CHOICES,default='Live')
	month = models.ForeignKey(Month, on_delete = models.SET_NULL, null = True)
	date =models.ForeignKey(Date, on_delete = models.SET_NULL, null = True)

	def __str__(self):
		return self.user.username

class Cape_Town_booking(models.Model):
	user = models.ForeignKey(User, on_delete= models.CASCADE)
	bootcamp_type = models.CharField('bootcamp_type',max_length=7,choices=BOOTCAMP_CHOICES,default='Live')
	month = models.ForeignKey(Month, on_delete = models.SET_NULL, blank = True, null = True)
	date =models.ForeignKey(Date, on_delete = models.SET_NULL, blank = True, null = True)

	def __str__(self):
		return self.user.username

class Durban_booking(models.Model):
	user = models.ForeignKey(User, on_delete= models.CASCADE)
	bootcamp_type = models.CharField('bootcamp_type',max_length=7,choices=BOOTCAMP_CHOICES,default='Live')
	month = models.ForeignKey(Month, on_delete = models.SET_NULL, blank = True, null = True)
	date =models.ForeignKey(Date, on_delete = models.SET_NULL, blank = True, null = True)

	def __str__(self):
		return self.user.username
