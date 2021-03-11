from rest_framework import routers
from Doctor_App import views as myapp_views


router = routers.DefaultRouter()
router.register(r'doctor', myapp_views.DoctorViewSet,basename='doctor_api')
router.register(r'Patient', myapp_views.PatientSet,basename='Patient_api')
router.register(r'Appointment', myapp_views.AppointmentSet,basename='Appointment_api')