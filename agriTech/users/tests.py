from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from users.models import User

class UserAPITests(APITestCase):
    def setUp(self):
        self.url = reverse('user-list')  
        self.cooperative = User.objects.create(
            type='cooperative',
            email='sam@gmail.com',
            password='s2M',
            phone_number='079869432',
            cooperative_name='Samuel'
        )

    def test_create_cooperative(self):
        data = {
            "type": "cooperative",
            "email": "fan@gmail.com",
            "password": "f@n34",
            "phone_number": "079169432",
            "cooperative_name": "Samuel"
        }
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["type"], "cooperative")

    def test_create_cooperative_missing_name(self):
        data = {
            "type": "cooperative",
            "email": "sam@example.com",
            "password": "s2M",
            "phone_number": "079869432",
           
        }
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("cooperative_name", response.data)

    def test_create_extension_officer(self):
        data = {
            "type": "extension_officer",
            "email": "fanabezabih@gmail.com",
            "password": "fa@bn",
            "phone_number": "0946564758",
            "officer_name": "fana bezabih",
            "cooperative": self.cooperative.pk
        }
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_extension_officer_missing_fields(self):
        data = {
            "type": "extension_officer",
            "email": "fanabezabih@gmail.com",
            "password": "fa@bn",
            "phone_number": "0946564758",
           
        }
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("officer_name", response.data)
        self.assertIn("cooperative", response.data)

    def test_create_farmer(self):
        data = {
            "type": "farmer",
            "email": "john@gmail.com",
            "password": "john123",
            "phone_number": "079865432",
            "farmer_name": "john hailay",
            "cooperative": self.cooperative.pk
        }
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_farmer_missing_fields(self):
        data = {
            "type": "farmer",
            "email": "john@gmail.com",
            "password": "john123",
            "phone_number": "079865432",

        }
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("farmer_name", response.data)
        self.assertIn("cooperative", response.data)

    def test_create_machine_supplier(self):
        data = {
            "type": "machine_supplier",
            "email": "sem@gmail.com",
            "password": "s@#m",
            "phone_number": "0934253647",
            "supplier_name": "Semhal Estifanos"
        }
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_machine_supplier_missing_name(self):
        data = {
            "type": "machine_supplier",
            "email": "sem@gmail.com",
            "password": "s@#m",
            "phone_number": "0934253647"
          
        }
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("supplier_name", response.data)