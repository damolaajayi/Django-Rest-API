from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import generics, permissions, renderers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

from .models import patient, Prescription
from .permissions import IsOwnerOrReadOnly
from .serializers import patientSerializer, PrescriptionSerializer, UserSerializer

class PatientHighlight(generics.GenericAPIView):
	queryset = patient.objects.all()
	renderer_classes = (renderers.StaticHTMLRenderer,)

	def get(self, request, *args, **kwargs):
		snippet = self.get_object()
		return Response(patient.highlighted)

# Create your views here.
@api_view(['GET'])
def api_root(request, format=None):
	return Response({
		'users': reverse('user-list', request=request, format=format),
		'patient': reverse('patient-list', request=request, format=format)
	})

class PatientList(generics.ListCreateAPIView):
	queryset = patient.objects.all()
	serializer_class = patientSerializer
	permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


	def perform_create(self, serializer):
		serializer.save(owner=self.request.user)

class PatientDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = patient.objects.all()
	serializer_class = patientSerializer
	permission_classes = (permissions.IsAuthenticatedOrReadOnly,
						  IsOwnerOrReadOnly, )


class PrescriptionList(generics.ListCreateAPIView):
	queryset = Prescription.objects.all()
	serializer_class = PrescriptionSerializer
	permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class PrescriptionDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Prescription.objects.all()
	serializer_class = PrescriptionSerializer
	permission_classes = (permissions.IsAuthenticatedOrReadOnly,
						  IsOwnerOrReadOnly, )

class UserList(generics.ListCreateAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer