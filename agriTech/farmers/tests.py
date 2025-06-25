from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from cooperatives.models import Cooperative
from farmers.models import Farmer

class FarmerAPITestCase(APITestCase):
    def setUp(self):
        # Create a Cooperative instance, including required fields
        self.cooperative = Cooperative.objects.create(
            cooperative_name="Abahinzi ba Kawa Kirehe",
            created_at="2025-06-22T14:00:00Z"
        )
        self.farmer_data = {
            "cooperative_id": self.cooperative.cooperative_id,  # <-- FIXED HERE
            "farmer_name": "Niyonzima Jean Pierre",
            "email": "niyonzima.jp@gmail.com",
            "password": "ikawaRwanda2025",
            "phone_number": "0788123456",
            "created_at": "2025-06-25T08:00:00Z"
        }
        self.farmer = Farmer.objects.create(
            cooperative_id=self.cooperative,  # <-- FIXED HERE
            farmer_name="Mukamana Aline",
            email="aline.mukamana@gmail.com",
            password="securepassRWA",
            phone_number="0722334455",
            created_at="2025-06-24T07:30:00Z"
        )

    def test_list_farmers(self):
        url = reverse("farmer-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, list)

    def test_create_farmer(self):
        url = reverse("farmer-list")
        response = self.client.post(url, self.farmer_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["farmer_name"], self.farmer_data["farmer_name"])
        self.assertEqual(response.data["phone_number"], self.farmer_data["phone_number"])
        self.assertEqual(response.data["email"], self.farmer_data["email"])

    def test_retrieve_farmer(self):
        url = reverse("farmer-detail", args=[self.farmer.farmer_id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["farmer_name"], self.farmer.farmer_name)
        self.assertEqual(response.data["phone_number"], self.farmer.phone_number)

    def test_update_farmer(self):
        url = reverse("farmer-detail", args=[self.farmer.farmer_id])
        data = {
            "cooperative_id": self.cooperative.cooperative_id,  # <-- FIXED HERE
            "farmer_name": "Mukamana Aline Uwase",
            "email": "aline.uwase@gmail.com",
            "password": "rwanda2025",
            "phone_number": "0733112233",
            "created_at": "2025-06-24T07:30:00Z"
        }
        response = self.client.put(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["farmer_name"], "Mukamana Aline Uwase")
        self.assertEqual(response.data["phone_number"], "0733112233")

    def test_delete_farmer(self):
        url = reverse("farmer-detail", args=[self.farmer.farmer_id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Farmer.objects.filter(farmer_id=self.farmer.farmer_id).exists())