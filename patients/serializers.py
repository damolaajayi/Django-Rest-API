from django.contrib.auth.models import User
from rest_framework import serializers
from .models import patient, Prescription

class patientSerializer(serializers.HyperlinkedModelSerializer):
	owner = serializers.ReadOnlyField(source='owner.username')

	#highlight = serializers.HyperlinkedIdentityField(
       # view_name='patient-highlight', format='html')
	
	class Meta:
		model = patient
		fields = ('Reg_No', 'first_name', 'Last_name', 'Email', 'Patient_Age','Gender',
				   'Contact_No', 'Patient_Address', 'owner',)


class UserSerializer(serializers.HyperlinkedModelSerializer):
	patient = serializers.PrimaryKeyRelatedField(many=True, queryset=patient.objects.all())

	class Meta:
		model = User
		fields = ('id', 'username', 'patient')


class PrescriptionSerializer(serializers.ModelSerializer):

	class Meta:
		model = Prescription
		fields = '__all__'

class UserSerializer(serializers.HyperlinkedModelSerializer):
	patient = serializers.PrimaryKeyRelatedField(many=True, queryset=Prescription.objects.all())

	class Meta:
		model = User
		fields = ('id', 'username', 'patient')
