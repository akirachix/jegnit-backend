from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from farmers.models import Farmer
from cooperatives.models import Cooperative
from machinery.models import Machinery
from lending_records.models import Lending_Record
from django.utils import timezone

class LendingRecordAPITestCase(APITestCase):
    def setUp(self):
        
        self.cooperative = Cooperative.objects.create(
            created_at=timezone.now()
        )
        
        self.farmer = Farmer.objects.create(
            cooperative_id=self.cooperative,
            created_at=timezone.now()
        )
       
        self.machinery = Machinery.objects.create(
            created_at=timezone.now()
        )
       
        self.lending_record = Lending_Record.objects.create(
            machinery_id=self.machinery,
            borrower_id=self.farmer,
            approved_by=self.cooperative,
            start_date="2025-06-24T10:00:00Z",
            end_date="2025-06-25T10:00:00Z",
            status="pending"
        )
        self.list_url = reverse("lending_records-list")
        self.detail_url = reverse("lending_records-detail", args=[self.lending_record.lending_id])

    def test_list_lending_records(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    def test_retrieve_lending_record(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['lending_id'], self.lending_record.lending_id)

    def test_create_lending_record(self):
        data = {
            "machinery_id": self.machinery.machinery_id,  
            "borrower_id": self.farmer.farmer_id,          
            "approved_by": self.cooperative.cooperative_id, 
            "start_date": "2025-06-26T10:00:00Z",
            "end_date": "2025-06-27T10:00:00Z",
            "status": "approved"
        }
        response = self.client.post(self.list_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Lending_Record.objects.count(), 2)

    def test_update_lending_record(self):
        data = {
            "machinery_id": self.machinery.machinery_id,
            "borrower_id": self.farmer.farmer_id,
            "approved_by": self.cooperative.cooperative_id,
            "start_date": "2025-06-28T10:00:00Z",
            "end_date": "2025-06-29T10:00:00Z",
            "status": "returned"
        }
        response = self.client.put(self.detail_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.lending_record.refresh_from_db()
        self.assertEqual(self.lending_record.status, "returned")

    def test_delete_lending_record(self):
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Lending_Record.objects.filter(pk=self.lending_record.lending_id).exists())