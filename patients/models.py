from django.db import models
from pygments import highlight
from pygments.formatters.html import HtmlFormatter
from pygments.lexers import get_all_lexers, get_lexer_by_name
import datetime



class patient(models.Model):
	SEX = (
		('M', 'Male'),
		('F', 'Female'),
		)
	
	Reg_No          = models.SmallIntegerField(primary_key=True)
	first_name      = models.CharField(max_length=25)
	Last_name       = models.CharField(max_length=25)
	Email           = models.EmailField(max_length=50)
	Patient_Age     = models.CharField(max_length=10)
	Gender          = models.CharField(max_length=6, choices=SEX)
	Contact_No      = models.BigIntegerField()
	Patient_Address = models.TextField(max_length=100)
	owner           = models.ForeignKey('auth.User', related_name='patient', on_delete=models.CASCADE)
	highlight       = models.TextField()
	time 			= models.DateTimeField(auto_now=True)

	
	def __str__(self):
		return "%s %s" % (self.first_name, self.Last_name)

	

class Prescription(models.Model):
	patient         = models.ForeignKey(patient, on_delete=models.CASCADE)
	Complaint       = models.TextField(max_length=300)
	Prescription    = models.TextField(max_length=200)
	Remarks         = models.TextField(max_length=100)
	Date            = models.DateTimeField('Date prescribed', auto_now=False, auto_now_add=True)

	class Meta:
		ordering = ('patient',)
	

	def __str__(self):
		return self.Prescription

	