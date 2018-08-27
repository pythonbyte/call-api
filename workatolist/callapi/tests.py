import pytz
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.test import APIClient
from django.urls import reverse

from datetime import datetime


from callapi.models import CallStart, CallEnd, PhoneBill
from callapi.serializers import CallStartSerializer, CallEndSerializer


class TestCallStart(APITestCase):
	def setUp(self):
		self.client = APIClient()

		self.valid_call = CallStart(source='9997073333', 
								call_id=190,
								destination= "9930940770", 
							timestamp=datetime(2002,3,11,11,11,10, 
											tzinfo=pytz.UTC))


		self.invalid_call = CallStart(source='9997073333', 
								call_id=190,
							timestamp=datetime(2002,3,11,11,11,10, 
											tzinfo=pytz.UTC))


	def test_create_callstart(self):
		old_count = CallStart.objects.count()
		self.valid_call.save()
		new_count = CallStart.objects.count()
		self.assertNotEqual(old_count, new_count)
	
	def test_create_valid_callstart(self):
		url = reverse('call-start')
		call = self.valid_call
		serializer = CallStartSerializer(call)
		response = self.client.post(url, data=serializer.data)
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)

	def test_get_method_callstart_endpoint(self):
		response = self.client.get(reverse('call-start'))
		self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

	def test_post_invalid_data(self):
		url = reverse('call-start')
		serializer = CallStartSerializer(self.invalid_call)
		data = serializer.data
		response = self.client.post(url, data=data)
		self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

	def test_post_call_same_call_id(self):
		self.valid_call.save()
		url = reverse('call-start')
		serializer = CallStartSerializer(self.valid_call)
		data = serializer.data
		response = self.client.post(url, data=data)
		self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)






class TestCallEnd(APITestCase):

	def setUp(self):
		self.client = APIClient()
		self.valid_callend = CallEnd(call_id='1',timestamp=datetime(2002,3,11,11,11,10, 
											tzinfo=pytz.UTC))


	def test_create_callend(self):
		old_count = CallEnd.objects.count()
		self.call.save()
		new_count = CallEnd.objects.count()
		self.assertNotEqual(old_count, new_count)

	def test_create_valid_callstart(self):
		url = reverse('call-end')
		call = self.valid_callend
		serializer = CallEndSerializer(call)
		response = self.client.post(url, data=serializer.data)
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)
	
	def test_get_method_callend_endpoint(self):
		response = self.client.get(reverse('call-end'))
		self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)








class TestPhoneBill(APITestCase):
	def setUp(self):
		self.client = APIClient()
		self.call = PhoneBill(subscriber='3199778899')


	def test_create_phonebill(self):
		old_count = PhoneBill.objects.count()
		self.call.save()
		new_count = PhoneBill.objects.count()
		self.assertNotEqual(old_count, new_count)

	def test_get_method_without_data_phonebill_endpoint(self):
		response = self.client.get(reverse('bills'))
		self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
