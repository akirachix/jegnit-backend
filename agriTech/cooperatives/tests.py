from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from cooperatives.models import Cooperative

class CooperativeAPITestCase(APITestCase):
    def setUp(self):
        self.coop_data = {
            "cooperative_name": "Koperative Tuzamurane",
            "email": "tuzamurane@coops.rw",
            "password": "ikazeRwanda2025",
            "phone_number": "0788456789",
            "created_at": "2025-06-24T09:15:00Z"
        }
        self.coop = Cooperative.objects.create(
            cooperative_name="Koperative Abahizi ba Kawa",
            email="abahizi.kawa@coops.rw",
            password="secretRwanda",
            phone_number="0722119988",
            created_at="2025-06-22T14:00:00Z"
        )

    def test_list_cooperatives(self):
        url = reverse("cooperative-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, list)

    def test_create_cooperative(self):
        url = reverse("cooperative-list")
        response = self.client.post(url, self.coop_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["cooperative_name"], self.coop_data["cooperative_name"])
        self.assertEqual(response.data["phone_number"], self.coop_data["phone_number"])
        self.assertEqual(response.data["email"], self.coop_data["email"])

    def test_retrieve_cooperative(self):
        url = reverse("cooperative-detail", args=[self.coop.cooperative_id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["cooperative_name"], self.coop.cooperative_name)
        self.assertEqual(response.data["phone_number"], self.coop.phone_number)

    def test_update_cooperative(self):
        url = reverse("cooperative-detail", args=[self.coop.cooperative_id])
        data = {
            "cooperative_name": "Koperative Abahizi ba Kawa Rwanda",
            "email": "abahizi.kawa.rw@coops.rw",
            "password": "rwanda2025",
            "phone_number": "0733221100",
            "created_at": "2025-06-22T14:00:00Z"
        }
        response = self.client.put(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["cooperative_name"], "Koperative Abahizi ba Kawa Rwanda")
        self.assertEqual(response.data["phone_number"], "0733221100")

    def test_delete_cooperative(self):
        url = reverse("cooperative-detail", args=[self.coop.cooperative_id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Cooperative.objects.filter(cooperative_id=self.coop.cooperative_id).exists())