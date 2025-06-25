from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from cooperatives.models import Cooperative
from farmers.models import Farmer

class FarmerAPITests(APITestCase):
    def setUp(self):
    
        self.user = User.objects.create_user(username='farmeruser', password='testpass')
        self.coop_user = User.objects.create_user(username='coopuser', password='coopass')
        self.cooperative = Cooperative.objects.create(
            user=self.coop_user,
            cooperative_name="Test Cooperative",
            email="test@coop.com",
            password="coopassword",
            phone_number="07896543289",
            created_at="2024-01-01T00:00"
        )
        self.farmer = Farmer.objects.create(
            user=self.user,
            cooperative_id=self.cooperative,
            farmer_name="Test Farmer",
            email="farmer@farm.com",
            password="farmpassword",
            phone_number="0987654321",
            created_at="2024-01-02T12:00"
        )

    def test_list_farmers(self):
        url = reverse('farmer-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(len(response.data) > 0)

    def test_create_farmer(self):
        user2 = User.objects.create_user(username='user2', password='pass2')
        url = reverse('farmer-list')
        data = {
            "user": user2.id,
            "cooperative_id": self.cooperative.cooperative_id,
            "farmer_name": "Another Farmer",
            "email": "another@farm.com",
            "password": "anotherpassword",
            "phone_number": "1122334455",
            "created_at": "2024-01-03T09:30"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Farmer.objects.count(), 2)

    def test_retrieve_farmer(self):
        url = reverse('farmer-detail', args=[self.farmer.farmer_id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['farmer_name'], "Test Farmer")

    def test_update_farmer(self):
        url = reverse('farmer-detail', args=[self.farmer.farmer_id])
        data = {
            "user": self.user.id,
            "cooperative_id": self.cooperative.cooperative_id,
            "farmer_name": "Updated Farmer",
            "email": "farmer@farm.com",
            "password": "farmpassword",
            "phone_number": "0987654321",
            "created_at": "2024-01-02T12:00"
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.farmer.refresh_from_db()
        self.assertEqual(self.farmer.farmer_name, "Updated Farmer")

    def test_delete_farmer(self):
        url = reverse('farmer-detail', args=[self.farmer.farmer_id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Farmer.objects.count(), 0)