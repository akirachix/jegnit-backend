from django.test import TestCase

# Create your tests here.
from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from cooperatives.models import Cooperative

class CooperativeAPITests(APITestCase):
    def setUp(self):
        # Create a user for the OneToOneField
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.cooperative = Cooperative.objects.create(
            user=self.user,
            cooperative_name="Test Cooperative",
            email="test@coop.com",
            password="testpassword",
            phone_number="1234567890",
            created_at="2024-01-01T00:00"
        )

    def test_list_cooperatives(self):
        url = reverse('cooperative-list')  # URL name from router
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(len(response.data) > 0)

    def test_create_cooperative(self):
        user2 = User.objects.create_user(username='user2', password='pass2')
        url = reverse('cooperative-list')
        data = {
            "user": user2.id,
            "cooperative_name": "Another Coop",
            "email": "another@coop.com",
            "password": "anotherpassword",
            "phone_number": "0987654321",
            "created_at": "2024-01-02T12:00"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Cooperative.objects.count(), 2)

    def test_retrieve_cooperative(self):
        url = reverse('cooperative-detail', args=[self.cooperative.cooperative_id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['cooperative_name'], "Test Cooperative")

    def test_update_cooperative(self):
        url = reverse('cooperative-detail', args=[self.cooperative.cooperative_id])
        data = {
            "user": self.user.id,
            "cooperative_name": "Updated Name",
            "email": "test@coop.com",
            "password": "testpassword",
            "phone_number": "1234567890",
            "created_at": "2024-01-01T00:00"
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.cooperative.refresh_from_db()
        self.assertEqual(self.cooperative.cooperative_name, "Updated Name")

    def test_delete_cooperative(self):
        url = reverse('cooperative-detail', args=[self.cooperative.cooperative_id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Cooperative.objects.count(), 0)
