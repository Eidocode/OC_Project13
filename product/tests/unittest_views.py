from django.test import TestCase
from django.urls import reverse

from product.models import Category, Brand, Device


class IndexViewTestCase(TestCase):
    """
    Tests for the index page.
    """
    def setUp(self):
        # Creating some test data for devices, categories, and brands
        self.category = Category.objects.create(name='Category')
        self.brand = Brand.objects.create(name='Brand')
        self.device1 = Device.objects.create(product=self.brand,
                                             device_user=None,
                                             inventory=None,
                                             immo=None,
                                             added_date='2023-04-10')
        self.device2 = Device.objects.create(product=self.brand,
                                             device_user=None,
                                             inventory=None,
                                             immo=None,
                                             added_date='2023-04-11')
        self.device3 = Device.objects.create(product=self.brand,
                                             device_user=None,
                                             inventory=None,
                                             immo=None,
                                             added_date='2023-04-12')
        self.device4 = Device.objects.create(product=self.brand,
                                             device_user=None,
                                             inventory=None,
                                             immo=None,
                                             added_date='2023-04-13')
        self.device5 = Device.objects.create(product=self.brand,
                                             device_user=None,
                                             inventory=None,
                                             immo=None,
                                             added_date='2023-04-14')

    def test_index_url_exists_at_location(self):
        """
        Checks that the index page is accessible at /
        """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_index_url_by_name(self):
        """
        Checks that the index page is accessible with name "index"
        """
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

    def test_index_url_uses_correct_template(self):
        """
        Checks that the index page uses the correct template
        """
        response = self.client.get(reverse('index'))
        self.assertTemplateUsed(response, 'product/index.html')
