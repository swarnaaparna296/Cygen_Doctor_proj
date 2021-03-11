from django.test import TestCase, Client
from Doctor_App.views import *
from Doctor_App.models import *
import json
from django.urls import reverse
from Doctor_App.serializers import *


# initialize the APIClient app
client = Client()


class CreateNewAppointmentTest(TestCase):
	""" Test module for inserting a new puppy """

	def setUp(self):
		self.valid_payload = {
				"appointment_date": "05/03/2021",
				"appointment_time": "09:09",
				"problem": "Health issue",
				"patient_name": 1,
				"doctor_name": 1
		}
		self.invalid_payload = {
				"appointment_date": "05-03-2021",
				"appointment_time": "09:09",
				"problem": "Health issue",
				"patient_name": 1,
				"doctor_name": 1
				}

	def test_create_valid_Appointment(self):
		response = self.client.post(
			reverse('api:Appointment_api-list'),
			data=json.dumps(self.valid_payload),
			content_type='application/json'
		)
		self.assertEqual(response,200)

	def test_create_invalid_Appointment(self):
		response = self.client.post(
			reverse('api:Appointment_api-list'),
			data=json.dumps(self.invalid_payload),
			content_type='application/json'
		)
		self.assertEqual(response, 400)