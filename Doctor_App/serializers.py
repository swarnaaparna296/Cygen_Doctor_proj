from rest_framework import serializers
from Doctor_App.models import *
from django.contrib.auth.models import User
from Doctor_App.views import *

class DoctorSerialzers(serializers.ModelSerializer):
	class Meta:
		model=Doctor
		fields = '__all__'


class PatientSerialzers(serializers.ModelSerializer):
	class Meta:
		model=Patient
		fields = '__all__'

class AppointmentSerialzers(serializers.ModelSerializer):
	class Meta:
		model=Appointment
		fields = '__all__'

	def to_representation(self, instance):
		return AppointmentSerialzers(instance).to_representation(instance)