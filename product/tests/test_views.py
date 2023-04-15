from django.test import TestCase
from django.urls import reverse

from product.models import Category, Brand, Product, Device, Cpu, DeviceUser, Inventory, CpuBrand


class IndexViewTest(TestCase):
    """
    Tests for the index page.
    """

    @classmethod
    def setUpTestData(cls):
        # Create test data
        Category.objects.create(name='Test Category')
        Brand.objects.create(name='Test Brand')
        CpuBrand.objects.create(name='Test CPU Brand')
        for i in range(6):
            Device.objects.create(
                product=Product.objects.create(
                    name=f'Test Product {i}',
                    category=Category.objects.get(name='Test Category'),
                    brand=Brand.objects.get(name='Test Brand'),
                ),
                device_user=DeviceUser.objects.create(
                    first_name=f'Test FName {i}',
                    last_name=f'Test LName {i}',
                    uid=f'Test UID {i}',
                ),
                inventory=Inventory.objects.create(
                    hostname=f'Test Hostname {i}',
                    serial=f'Test Serial Number {i}',
                    cpu=Cpu.objects.create(
                        name=f'Test CPU {i}',
                        cpu_brand=CpuBrand.objects.get(name='Test CPU Brand'),
                    )
                ),
            )
            print(f'Test Device {i} created')

    def test_index_view_uses_correct_template(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'product/index.html')

    def test_index_view_context_data(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        print(response.context['devices'])
        self.assertQuerysetEqual(
            response.context['devices'],
            [
                '<Device: Test Hostname 4>', '<Device: Test Hostname 3>',
                '<Device: Test Hostname 2>', '<Device: Test Hostname 1>',
                '<Device: Test Hostname 0>'
            ]
        )
        self.assertDictEqual(response.context['types'], {'Test Category': 6})
        self.assertDictEqual(response.context['brands'], {'Test Brand': 6})
