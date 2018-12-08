from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import generics, permissions, renderers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse


from .models import DoctorInfo
from .permissions import IsOwnerOrReadOnly
from .serializers import DoctorInfoSerializer, UserSerializer

# Create your views here.
'''
@api_view(['GET'])
def api_root(request, format=None):
	return Response({
		'users': reverse('user-list', request=request, format=format),
		'doctor': reverse('doctor-list', request=request, format=format)
	})
'''
class DoctorList(generics.ListCreateAPIView):
	queryset = DoctorInfo.objects.all()
	serializer_class = DoctorInfoSerializer

class DoctorDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = DoctorInfo.objects.all()
	serializer_class = DoctorInfoSerializer

class UserList(generics.ListCreateAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer