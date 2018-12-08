from django.db import models
from patients.models import patient
# Create your models here.
class DoctorInfo(models.Model):
	SEX = (
		('M', 'Male'),
		('F', 'Female'),
		)
	ID         = models.SmallIntegerField(primary_key=True)
	Name       = models.CharField(max_length=100)
	Age        = models.CharField(max_length=50)
	Contact_No = models.BigIntegerField(null=True)
	Gender     = models.CharField(max_length=6, choices=SEX)
	Department = models.CharField(max_length=100)

	def __str__(self):
		return self.Name
