from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
	path('doctor/', views.DoctorList.as_view(), name='doctor-list'),
	path('doctor/<int:pk>/', views.DoctorDetail.as_view(), name='doctor-detail'),
	path('users/', views.UserList.as_view(), name='user-list'),
	path('users/<int:pk>/', views.UserDetail.as_view(), name='user-detail'),
	#path('', views.api_root),
]