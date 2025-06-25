from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from cooperatives.models import Cooperative
from extension_officer.models import Extension_Officer
# Create your tests here.

class ExtensionOfficerAPITestCase(APITestCase):
    def setUp(self):
        import datetime
        self.cooperative = Cooperative.objects.create(
            cooperative_name="Cooperative",
            email="cooperative@gmail.com",
            password="@#cooperative",
            phone_number="+2547438234",
            created_at=datetime.datetime.now()
)


          
        
        self.extension_officer_data = {
            "cooperative_id": self.cooperative.cooperative_id,
            "officer_name": "Umrava Muziyere",
            "email": "umrava@gmail.com",
            "password": "umr@#va",
            "phone_number": "+254678982345",
            "created_at": "2025-03-08T12:00:00Z"
        }
        self.list_url = reverse('extension officer-list')

    def test_create_extension_officer(self):
        response = self.client.post(self.list_url, self.extension_officer_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Extension_Officer.objects.count(), 1)
        self.assertEqual(Extension_Officer.objects.get().officer_name, "Umrava Muziyere")

    def test_list_extension_officers(self):
        Extension_Officer.objects.create(
            cooperative_id= self.cooperative,
            officer_name="Umrava Muziyere",
            email="umrava@gmail.com",
            password="umr@#va",
            phone_number="+254678982345",
            created_at="2025-03-08T12:00:00Z"
        )
        response = self.client.get(self.list_url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['officer_name'], "Umrava Muziyere")

    def test_retrieve_extension_officer(self):
        officer = Extension_Officer.objects.create(
            cooperative_id=self.cooperative,
            officer_name="Daniella Syombua",
            email="syombua@gmail.com",
            password="dan#$iela",
            phone_number="+251923453245",
            created_at="2025-10-12T14:30:00Z"
        )
        url = reverse('extension officer-detail', args=[officer.extension_id])
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['officer_name'], "Daniella Syombua")

    def test_update_extension_officer(self):
        officer = Extension_Officer.objects.create(
            cooperative_id=self.cooperative,
            officer_name="Umrava Muziyere",
            email="umrava@gmail.com",
            password="umr@#va",
            phone_number="+254678982345",
            created_at="2025-03-08T12:00:00Z"
        )
        url = reverse('extension officer-detail', args=[officer.extension_id])
        updated_data = self.extension_officer_data.copy()
        updated_data['officer_name'] = "Umrava Updated"
        updated_data['cooperative_id'] = self.cooperative.cooperative_id
        response = self.client.put(url, updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        officer.refresh_from_db()
        self.assertEqual(officer.officer_name, "Umrava Updated")

    def test_delete_extension_officer(self):
        officer = Extension_Officer.objects.create(
            cooperative_id=self.cooperative,
            officer_name="Umrava Muziyere",
            email="umrava@gmail.com",
            password="umr@#va",
            phone_number="+254678982345",
            created_at="2025-03-08T12:00:00Z"
        )
        url = reverse('extension officer-detail', args=[officer.extension_id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Extension_Officer.objects.count(), 0)