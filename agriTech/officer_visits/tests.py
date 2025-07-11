from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from officer_visits.models import Officer_Visit
from farmers.models import Farmer
from cooperatives.models import Cooperative
from extension_officer.models import Extension_Officer
from django.utils import timezone

class OfficerVisitAPITestCase(APITestCase):
    def setUp(self):
        
        self.cooperative = Cooperative.objects.create(
            created_at=timezone.now()
        )
       
        self.farmer = Farmer.objects.create(
            cooperative_id=self.cooperative,
            created_at=timezone.now()
        )
       
        self.officer = Extension_Officer.objects.create(
            cooperative_id=self.cooperative,
            created_at=timezone.now()
        )
        self.visit = Officer_Visit.objects.create(
            officer_id=self.officer,
            farmer_id=self.farmer,
            visit_date=timezone.now(),
            notes="Initial visit notes."
        )
        self.list_url = reverse("officer_visits-list")
        self.detail_url = reverse("officer_visits-detail", args=[self.visit.visits_id])

    def test_list_officer_visits(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    def test_retrieve_officer_visit(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["visits_id"], self.visit.visits_id)

    def test_create_officer_visit(self):
        data = {
            "officer_id": self.officer.pk,
            "farmer_id": self.farmer.pk,
            "visit_date": timezone.now().isoformat(),
            "notes": "Routine follow-up."
        }
        response = self.client.post(self.list_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Officer_Visit.objects.count(), 2)

    def test_update_officer_visit(self):
        data = {
            "officer_id": self.officer.pk,
            "farmer_id": self.farmer.pk,
            "visit_date": timezone.now().isoformat(),
            "notes": "Updated visit notes."
        }
        response = self.client.put(self.detail_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.visit.refresh_from_db()
        self.assertEqual(self.visit.notes, "Updated visit notes.")

    def test_delete_officer_visit(self):
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Officer_Visit.objects.filter(pk=self.visit.visits_id).exists())