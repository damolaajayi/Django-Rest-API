from django.contrib.auth.models import User
from rest_framework import serializers
from .models import DoctorInfo

class DoctorInfoSerializer(serializers.HyperlinkedModelSerializer):
	owner = serializers.ReadOnlyField(source='owner.username')

	class Meta:
		model = DoctorInfo

		fields = ('ID', 'Name', 'Age', 'Contact_No', 'Gender', 'Department', 'owner', )



class UserSerializer(serializers.HyperlinkedModelSerializer):
	#Doctor = serializers.PrimaryKeyRelatedField(many=True, queryset=DoctorInfo.objects.all())

	class Meta:
		model = User
		fields = ('id', 'username', )
