from django.template.loader import rendr_to_string
from django.test import TestCase,Client
from codeprinter.models import WebInfo,Classify,Company,Product
from codeprinter.views import *

class ViewTest(TestCase):
	def setUp(self):
		self.client_stub=Client()
	def test_view_home_route(self):
		response=self.client_stub.get('/')
		self.assertEquals(response.status_code,200)

	def test_view_classify(self):
		response=self.client_stub.get('/class/1/')
		self.assertEquals(response.status_code,200)


