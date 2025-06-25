from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from datetime import datetime, timedelta
from .models import Auth_Token

class AuthTokenAPITestCase(APITestCase):
    def setUp(self):
        self.auth_token_data = {
            "token": "RWANDA123456TOKEN",
            "expired_at": "2025-07-01T12:00:00Z"
        }
        self.token_instance = Auth_Token.objects.create(
            token="KIGALI987654TOKEN",
            expired_at="2025-06-30T18:00:00Z"
        )

    def test_list_auth_tokens(self):
        url = reverse("auth_token-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, list)

    def test_create_auth_token(self):
        url = reverse("auth_token-list")
        response = self.client.post(url, self.auth_token_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["token"], self.auth_token_data["token"])
        self.assertEqual(response.data["expired_at"], self.auth_token_data["expired_at"])

    def test_retrieve_auth_token(self):
        url = reverse("auth_token-detail", args=[self.token_instance.tokens_id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["token"], self.token_instance.token)

    def test_update_auth_token(self):
        url = reverse("auth_token-detail", args=[self.token_instance.tokens_id])
        data = {
            "token": "RWANDAUPDATEDTOKEN",
            "expired_at": "2025-07-10T10:00:00Z"
        }
        response = self.client.put(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["token"], "RWANDAUPDATEDTOKEN")
        self.assertEqual(response.data["expired_at"], "2025-07-10T10:00:00Z")

    def test_delete_auth_token(self):
        url = reverse("auth_token-detail", args=[self.token_instance.tokens_id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Auth_Token.objects.filter(tokens_id=self.token_instance.tokens_id).exists())