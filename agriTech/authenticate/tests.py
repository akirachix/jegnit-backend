from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from authenticate.models import Auth_Token
from django.utils import timezone
from datetime import timedelta

class AuthTokenAPITests(APITestCase):
    def setUp(self):
        self.token_instance = Auth_Token.objects.create(
            token='abc123',
            expired_at=timezone.now() + timedelta(days=1)
        )

    def test_list_auth_tokens(self):
        url = reverse('authentication-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(len(response.data) > 0)

    def test_create_auth_token(self):
        url = reverse('authentication-list')
        data = {
            "token": "def456",
            "expired_at": (timezone.now() + timedelta(days=2)).isoformat()
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Auth_Token.objects.count(), 2)

    def test_retrieve_auth_token(self):
        url = reverse('authentication-detail', args=[self.token_instance.tokens_id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['token'], "abc123")

    def test_update_auth_token(self):
        url = reverse('authentication-detail', args=[self.token_instance.tokens_id])
        data = {
            "token": "updatedtoken",
            "expired_at": (timezone.now() + timedelta(days=3)).isoformat()
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.token_instance.refresh_from_db()
        self.assertEqual(self.token_instance.token, "updatedtoken")

    def test_delete_auth_token(self):
        url = reverse('authentication-detail', args=[self.token_instance.tokens_id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Auth_Token.objects.count(), 0)