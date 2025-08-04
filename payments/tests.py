from django.test import TestCase

# Create your tests here.
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import FarmerPayment, CooperativePayment
from cooperatives.models import Cooperative
from farmers.models import Farmer
from machine_supplier.models import Machine_Supplier
from django.utils import timezone
from decimal import Decimal
class FarmerPaymentAPITestCase(APITestCase):
    def setUp(self):
        self.cooperative = Cooperative.objects.create(
            cooperative_name="AgriCreds",
            email="agricreds@gmail.com.com",
            password="agri_20@T",
            phone_number="+2507123456789",
            created_at=timezone.now()
        )
        self.farmer = Farmer.objects.create(
            farmer_name="Jace Muyiza",
            email="jacemuyiza@gmail.com",
            password="Nyina@7890",
            phone_number="+2507987654321",
            created_at=timezone.now(),
            cooperative_id=self.cooperative
        )
        self.url = reverse("farmer-payment-list")
        self.payment_data = {
            "amount": "100.00",
            "payment_method": "Mobile money",
            "status": "Paid",
            "paid_at": timezone.now(),
            "farmer": self.farmer.pk,
            "cooperative": self.cooperative.cooperative_id,
        }
        self.payment = FarmerPayment.objects.create(
            amount=Decimal("50.00"),
            payment_method="Mobile money",
            status="Pending",
            paid_at=timezone.now(),
            farmer=self.farmer,
            cooperative=self.cooperative
        )
    def test_list_farmer_payments(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    def test_create_farmer_payment(self):
        response = self.client.post(self.url, self.payment_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(FarmerPayment.objects.count(), 2)
    def test_retrieve_farmer_payment(self):
        url = reverse("farmer-payment-detail", args=[self.payment.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("amount", response.data)
    def test_create_invalid_farmer_payment(self):
        data = self.payment_data.copy()
        data["amount"] = ""
        response = self.client.post(self.url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
class CooperativePaymentAPITestCase(APITestCase):
    def setUp(self):
        self.cooperative = Cooperative.objects.create(
            cooperative_name="Emeline Giso",
            email="emelinegiso@gmail.com",
            password="Giso!@20",
            phone_number="+25072233445566",
            created_at=timezone.now()
        )
        self.supplier = Machine_Supplier.objects.create(
            supplier_name="Girmay supplies",
            email="girmaysupplies@mail.com",
            password="gima@657",
            phone_number="+25071122334455",
            created_at=timezone.now()
        )
        self.url = reverse("cooperative-payment-list")
        self.payment_data = {
            "amount": "250.00",
            "payment_method": "Bank Transfer",
            "status": "Completed",
            "paid_at": timezone.now(),
            "cooperative": self.cooperative.cooperative_id,
            "supplier": self.supplier.supplier_id,
        }
        self.payment = CooperativePayment.objects.create(
            amount=Decimal("75.00"),
            payment_method="Mobile money",
            status="Processing",
            paid_at=timezone.now(),
            cooperative=self.cooperative,
            supplier=self.supplier
        )
    def test_list_cooperative_payments(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    def test_create_cooperative_payment(self):
        response = self.client.post(self.url, self.payment_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(CooperativePayment.objects.count(), 2)
    def test_retrieve_cooperative_payment(self):
        url = reverse("cooperative-payment-detail", args=[self.payment.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("amount", response.data)
    def test_create_invalid_cooperative_payment(self):
        data = self.payment_data.copy()
        data["amount"] = ""
        response = self.client.post(self.url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)