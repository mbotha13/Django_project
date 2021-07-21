from django.db import models

BOOTCAMP_CHOICES=(
		('LIVE','Live'),
		('REMOTE','Remote'),
	)

# Create your models here.
class booking(models.Model):
	name = models.CharField('student name', max_length=55)
	bootcamp_type = models.CharField('bootcamp_type',max_length=7,choices=BOOTCAMP_CHOICES,default='Live')
	bootcamp_month = models.CharField('bootcamp month',max_length=10)
	camp_date =models.CharField('bootcamp date', max_length=10)

	def __str__(self):
		return self.name


class Cpt_booking(models.Model):
	name = models.CharField('student name', max_length=55)
	bootcamp_type = models.CharField('bootcamp_type',max_length=7,choices=BOOTCAMP_CHOICES,default='Live')
	bootcamp_month = models.CharField('bootcamp month',max_length=10)
	camp_date =models.CharField('bootcamp date', max_length=10)

	def __str__(self):
		return self.name

class Dbn_bokking(models.Model):
	name = models.CharField('student name', max_length=55)
	bootcamp_type = models.CharField('bootcamp_type',max_length=7,choices=BOOTCAMP_CHOICES,default='Live')
	bootcamp_month = models.CharField('bootcamp month',max_length=10)
	camp_date =models.CharField('bootcamp date', max_length=10)

	def __str__(self):
		return self.name