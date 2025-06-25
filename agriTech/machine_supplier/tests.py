from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from machine_supplier.models import Machine_Supplier
from django.utils import timezone

# Create your tests here.

class MachineSupplierAPITestCase(APITestCase):
    def setUp(self):
        self.machine_supplier_data = {
            "supplier_name": "Agro Machines",
            "officer_name": "Umrava Muyizere",
            "email": "agro@gmail.com",
            "password": "agro@p@ssw#rd",
            "phone_number": "+254939235242",
            "created_at": timezone.now().isoformat()
        }
        self.list_url = reverse('machine supplier-list')

    def test_create_machine_supplier(self):
        response = self.client.post(self.list_url, self.machine_supplier_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Machine_Supplier.objects.count(), 1)
        self.assertEqual(Machine_Supplier.objects.get().supplier_name, "Agro Machines")

    def test_list_machine_suppliers(self):
        Machine_Supplier.objects.create(
            supplier_name="Agro Machines",
            officer_name="Umrava Muyizere",
            email="agro@gmail.com",
            password="agro@p@ssw#rd",
            phone_number="+254939235242",
            created_at=timezone.now()
        )
        response = self.client.get(self.list_url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['supplier_name'], "Agro Machines")

    def test_retrieve_machine_supplier(self):
        supplier = Machine_Supplier.objects.create(
            supplier_name="Agro Machines",
            officer_name="Umrava Muyizere",
            email="agro@gmail.com",
            password="agro@p@ssw#rd",
            phone_number="+254939235242",
            created_at=timezone.now()
        )
        url = reverse('machine supplier-detail', args=[supplier.supplier_id])
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['supplier_name'], "Agro Machines")

    def test_update_machine_supplier(self):
        supplier = Machine_Supplier.objects.create(
            supplier_name="Agro Machines",
            officer_name="Umrava Muyizere",
            email="agro@gmail.com",
            password="agro@p@ssw#rd",
            phone_number="+254939235242",
            created_at=timezone.now()
        )
        url = reverse('machine supplier-detail', args=[supplier.supplier_id])
        updated_data = {
            "supplier_name": "Agro Machines",
            "officer_name": "Umrava Muyizere",
            "email": "agro@gmail.com",
            "password": "agro@p@ssw#rd",
            "phone_number": "+254939235242",
            "created_at": timezone.now().isoformat()
        }
        response = self.client.put(url, updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        supplier.refresh_from_db()
        self.assertEqual(supplier.supplier_name, "Agro Machines")

    def test_delete_machine_supplier(self):
        supplier = Machine_Supplier.objects.create(
            supplier_name="Agro Machines",
            officer_name="Umrava Muyizere",
            email="agro@gmail.com",
            password="agro@p@ssw#rd",
            phone_number="+254939235242",
            created_at=timezone.now()
        )
        url = reverse('machine supplier-detail', args=[supplier.supplier_id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Machine_Supplier.objects.count(), 0)