from django.test import TestCase

# Create your tests here.
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Machinery


class MachineryAPITests(APITestCase):
    def setUp(self):
        self.machinery_data = {
            "name": "Tractor",
            "description": "Heavy duty farming tractor",
            "status": "available",
            "added_by": "admin",
            "created_at": "2025-06-24T10:00:00Z"
        }
    def test_create_machinery(self):
        url = reverse('machinery-list')
        response = self.client.post(url, self.machinery_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['name'], 'Tractor')

    def test_list_machinery(self):
        Machinery.objects.create(**self.machinery_data)
        url = reverse('machinery-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

        
    def test_get_single_machinery(self):
        machinery = Machinery.objects.create(**self.machinery_data)
        url = reverse('machinery-detail', args=[machinery.pk])
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Tractor')

