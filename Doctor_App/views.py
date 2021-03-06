from django.shortcuts import render
from rest_framework.response import Response
from django.http import HttpResponse
# from rest_framework.views import APIView
from rest_framework import status, viewsets
from django.contrib.auth.models import User
from Doctor_App.models import *
from Doctor_App.serializers import *
from datetime import datetime, date
import requests

class DoctorViewSet(viewsets.ModelViewSet):
	serializer_class = DoctorSerialzers
	def get_queryset(self):
		name=self.request.query_params.get('doc_name')
		if name is not None:
			queryset =Doctor.objects.filter(name=name)
			return queryset
		else:
			queryset = Doctor.objects.all()
			return queryset

class PatientSet(viewsets.ModelViewSet):
	serializer_class = PatientSerialzers
	queryset = Patient.objects.all()


class AppointmentSet(viewsets.ModelViewSet):
	serializer_class = AppointmentSerialzers

	def get_queryset(self):
		queryset = Appointment.objects.all()
		return queryset

	def create(self, request):

		serializer = AppointmentSerialzers(data=request.data)

		queryset = Appointment.objects.filter(appointment_date=self.request.data['appointment_date'],
									patient_name=self.request.data['patient_name'],
									doctor_name=self.request.data['doctor_name'])
		if queryset:
			return Response({"Message":'Already exist on this date, please try to take another date.'}, status=status.HTTP_200_OK)
		else:

			if serializer.is_valid():
					serializer.save()
					return Response(serializer.data,status=status.HTTP_201_CREATED)
