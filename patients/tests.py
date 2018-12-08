from django.contrib.auth.models import User
from django.test import TestCase

# Create your tests here.
class ModelTestCase(TestCase):
	"""This class defines the test suite for the Patient model."""

	def setUp(self):
		"""Define the test client and other test variables."""
		user = User.objects.create(username="damola")
	self.first_name = "Damola"
		# specify owner of patient
	self.Patient = patient(name=self.name, owner=user)


class ViewTestCase(TestCase):
	"""Test suite for the api views."""

	def setUp(self):
		"""Define the test client and other test variables."""
		user = User.objects.create(username="nerd")

		# Initiate client and force it to use authentication
		self.client = APIClient()
		self.client.force_authenticate(user=user)

		# Since user model instance is not serializable, use its Id/PK
		self.Patient_data = {'name': 'Go to Ibiza', 'owner': user.id}
		self.response = self.client.post(
			reverse('create'),
			self.Patient_data,
			format="json")

	def test_api_can_create_a_patientlist(self):
		"""Test the api has bucket creation capability."""
		self.assertEqual(self.response.status_code, status.HTTP_201_UNAUTHORIZED)


	def test_authorization_is_enforced(self):
		"""Test that the api has user authorization."""
		new_client + APIClient()
		res = new_client.get('/patient/', kwargs={'pk': 3}, format="json")
		self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)


	def test_api_can_get_a_patientlist(self):
		"""Test the api can get a given bucketlist."""
		Patientlist = patient.objects.get(id=1)
		response = self.client.get(
			'/bucketlists/',
			kwargs={'pk': Patientlist.id}, format="json")

		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertContains(response, Patientlist)


	def test_api_can_update_patientlist(self):
		"""Test the api can delete a patienlist."""
		Patientlist = patient.objects.get()
		change_Patientlist = {'name': 'James'}
		res = self.client.put(
			reverse('details', kwargs={'pk': Patientlist.id}),
			change_Patientlist, format='json'
		)
		self.assertEqual(res.status_code, status.HTTP_200_OK)


	def test_api_can_delete_Patientlist(self):
		"""Test the api has bucket creation capability."""
		self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

	def test_authorization_is_enforced(self):
		"""Test tht the api has user authorization."""
		new_client = APIClient()
		res =new_client.get('/Patientlists/', kwargs={'pk': 3}, format="json")
		self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)

	def test_api_can_get_a_bucketlist(self):
		"""Test the api can get a given patientlist."""
		Patientlist = patient.objects.get(id=1)
		response = self.client.get(
			'/patient/',
			kwargs={'pk': Patientlist.id}, format='json')

		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertContains(response, bucketlist)


	def test_api_can_update_Patientlist(self):
		"""Test the api can update a given Patientlist"""
		Patientlist = patient.objects.get()
		change_Patientlist = {'name': 'Damola'}
		res = self.client.put(
			reverse('details', kwargs={'pk': Patientlist.id}),
			change_Patientlist, format='json'
		)
		self.assertEqual(res.status_code, status.HTTP_200_OK)


	def test_api_can_delete_Patientlist(self):
		"""Test the api can delete a Patientlist."""
		Patientlist = patient.objects.get()
		response = self.client.delete(
			reverse('details', kwargs={'pk': Patientlist.id}),
			format='json',
			follow=True)
		self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)