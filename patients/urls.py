from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.schemas import get_schema_view
from patients import views

schema_view = get_schema_view(title='Pastebin API')


urlpatterns = [
	path('schema/', schema_view),
	path('patient/', views.PatientList.as_view(), name='patient-list'),
	path('patient/<int:pk>/', views.PatientDetail.as_view(), name='patient-detail'),
	path('patient/<int:pk>/highlight/', 
		views.PatientHighlight.as_view(), name='patient-highlight'),
	path('prescription/', views.PrescriptionList.as_view(), name='Prescription-list'),
	path('prescription/<int:pk>/', views.PrescriptionDetail.as_view(), name='Prescription-detail'),
	path('users/', views.UserList.as_view(), name='user-list'),
	path('users/<int:pk>/', views.UserDetail.as_view(), name='user-detail'),
	path('', views.api_root),
]

urlpatterns = format_suffix_patterns(urlpatterns)