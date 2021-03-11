from django.db import models
from django.contrib.auth.models import User

class Doctor(models.Model):
	name = models.CharField(max_length=20,null=True)
	speciality = models.CharField(max_length=20,null=True)
	
	def __str__(self):
		return "%s" %(self.name)

class Patient(models.Model):
	patient_name = models.CharField(max_length=20,null=True)
	problem = models.CharField(max_length=20,null=True)
	
	def __str__(self):
		return "%s" %(self.patient_name)

class Appointment(models.Model):
	appointment_date = models.CharField(max_length=20,null=True)
	appointment_time = models.CharField(max_length=20,null=True)
	patient_name = models.ForeignKey(Patient, blank=True,on_delete=models.CASCADE)
	doctor_name = models.ForeignKey(Doctor, blank=True,on_delete=models.CASCADE)
	problem = models.TextField()
	
	def __str__(self):
			return "%s" %(self.patient_name.patient_name)