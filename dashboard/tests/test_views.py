from datetime import datetime
from django.test import TestCase, Client
from django.core import management
from django.db import connections
from django.urls import reverse

from dashboard.forms import SearchForm
from dashboard.views import get_devices_by_brand, get_devices_by_entities, \
    get_devices_by_os, count_devices_by_month
from product.models import Brand, Device, Entity

import tools.func_for_tests as tools


class DashboardViewTestCase(TestCase):
    """
    Test cases for the dashboard view
    """
    def setUp(self):
        # Create User object
        self.client = Client()
        self.username = 'test_user'
        self.password = 'test_password'
        self.user = tools.create_user_for_test(self.username, self.password)
        self.client.force_login(self.user)
        # Create tests data
        tools.create_tests_data()

    @classmethod
    def tearDownClass(cls):
        # Call super to close connections and remove data from the database
        super().tearDownClass()
        # Delete the test database
        management.call_command('flush', verbosity=0, interactive=False)
        # Disconnect from the test database
        connections['default'].close()

    def test_dashboard_url_exists_at_location(self):
        """
        Test that the dashboard url exists at the location
        """
        response = self.client.get('/dashboard/')
        self.assertEqual(response.status_code, 200)

    def test_dashboard_url_accessible_by_name(self):
        """
        Test that the dashboard url is accessible by name
        """
        response = self.client.get(reverse('dashboard'))
        self.assertEqual(response.status_code, 200)

    def test_dashboard_view_uses_correct_template(self):
        """
        Test that the dashboard view uses the correct template
        """
        response = self.client.get(reverse('dashboard'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'dashboard/dashboard.html')

    def test_dashboard_view_with_device_type(self):
        """
        Test if the dashboard view with device type is accessible
        """
        response = self.client.get(reverse(
            'dashboard_filter', args=['All devices']
        ))
        self.assertEqual(response.status_code, 200)

    def test_dashboard_view_with_year(self):
        """
        Test if the dashboard view with year is accessible
        """
        response = self.client.get(reverse(
            'dashboard_type_year', args=['All devices', 2023])
        )
        self.assertEqual(response.status_code, 200)

    def test_get_devices_by_brand(self):
        """
        Test if get_devices_by_brand returns correct devices count
        """
        qs_devices = Device.objects.all()
        queryset_brands = Brand.objects.all()
        devices_by_brand = get_devices_by_brand(queryset_brands, qs_devices)
        self.assertEqual(devices_by_brand['Test_Brand'], 20)

    def test_get_devices_by_entities(self):
        """
        Test if get_devices_by_entities returns correct devices count
        """
        qs_devices = Device.objects.all()
        qs_entities = Entity.objects.all()
        devices_by_entities = get_devices_by_entities(qs_entities, qs_devices)
        self.assertEqual(devices_by_entities['Test_Entity'], 20)

    def test_get_devices_by_os(self):
        """
        Test if get_devices_by_os returns correct devices count
        """
        qs_devices = Device.objects.all()
        devices_by_os = get_devices_by_os(qs_devices)
        self.assertEqual(devices_by_os['Test_OS'], 20)

    def test_count_devices_by_month(self):
        """
        Test if count_devices_by_month returns correct devices count
        """
        qs_devices = Device.objects.all()
        year = datetime.now().year
        months_count = count_devices_by_month(qs_devices, year)
        self.assertEqual(months_count[datetime.now().strftime("%b")], 20)

    def test_advanced_search_exists_at_location(self):
        """
        Test if the advanced search exists at the location
        """
        response = self.client.get('/dashboard/advanced_search/')
        self.assertEqual(response.status_code, 200)

    def test_advanced_search_uses_correct_template(self):
        """
        Test if the advanced search view uses the correct template
        """
        response = self.client.get(reverse('advanced_search'))
        self.assertTemplateUsed(response, 'dashboard/advanced_search.html')

    def test_advanced_search_is_valid(self):
        """
        Test if the advanced search view is valid
        """
        form_data = {
            'search': 'Test',
            'search_filter': 'device',
            'brand_filter': 'All',
            'type_filter': 'All',
            'radio_device_user': 'All'
        }
        self.assertTrue(SearchForm(data=form_data).is_valid())
        response = self.client.get(reverse('advanced_search'), form_data)
        self.assertEqual(response.status_code, 200)

    def test_advanced_search_is_not_valid(self):
        """
        Test if the advanced search view is not valid
        """
        form_data = {
            'search_filter': 'device',
            'brand_filter': 'Test Brand',
            'type_filter': 'Test Category',
            'radio_device_user': 'With'
        }
        self.assertFalse(SearchForm(data=form_data).is_valid())
        response = self.client.get(reverse('advanced_search'), form_data)
        self.assertEqual(response.status_code, 200)

    def test_advanced_search_filters_by_entity(self):
        """
        Test the advanced search view filters by entity
        """
        form_data = {
            'search': 'Test',
            'search_filter': 'entity',
            'brand_filter': 'Test_Brand',
            'type_filter': 'Test_Category',
            'radio_device_user': 'With'
        }
        self.assertTrue(SearchForm(data=form_data).is_valid())
        response = self.client.get(reverse('advanced_search'), form_data)
        self.assertContains(response, form_data['search'])
        self.assertEqual(len(response.context['result_process']), 20)

    def test_advanced_search_filters_by_device(self):
        """
        Test the advanced search view filters by device
        """
        form_data = {
            'search': 'Test',
            'search_filter': 'device',
            'brand_filter': 'Test_Brand',
            'type_filter': 'Test_Category',
            'radio_device_user': 'With'
        }
        self.assertTrue(SearchForm(data=form_data).is_valid())
        response = self.client.get(reverse('advanced_search'), form_data)
        self.assertContains(response, form_data['search'])
        self.assertEqual(len(response.context['result_process']), 20)

    def test_advanced_search_filters_by_device_user(self):
        """
        Test the advanced search view filters by device_user
        """
        form_data = {
            'search': 'FName',
            'search_filter': 'user',
            'brand_filter': 'Test_Brand',
            'type_filter': 'Test_Category',
            'radio_device_user': 'With'
        }
        self.assertTrue(SearchForm(data=form_data).is_valid())
        response = self.client.get(reverse('advanced_search'), form_data)
        self.assertContains(response, form_data['search'])
        self.assertEqual(len(response.context['result_process']), 20)

    def test_advanced_search_filters_by_device_without_user(self):
        """
        Test the advanced search view filters by brand
        """
        form_data = {
            'search': 'Test',
            'search_filter': 'device',
            'brand_filter': 'Test_Brand',
            'type_filter': 'Test_Category',
            'radio_device_user': 'Without'
        }
        self.assertTrue(SearchForm(data=form_data).is_valid())
        response = self.client.get(reverse('advanced_search'), form_data)
        self.assertContains(response, form_data['search'])
        self.assertEqual(len(response.context['result_process']), 0)
