from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse
from django.core import management
from django.db import connections

from product.models import DeviceUser, Device, Category, Brand, CpuBrand, \
    Product, Inventory, Cpu, Location, OperatingSystem, Entity

import tools.func_for_tests as tools


class DeviceUserViewTestCase(TestCase):
    """
    Test cases for the device user view
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

    def test_last_device_users_url_exists_at_location(self):
        """
        Test that the device users url exists at the location
        """
        response = self.client.get('/product_user/last_users/')
        self.assertEqual(response.status_code, 200)

    def test_last_device_users_url_accessible_by_name(self):
        """
        Test that the device users url is accessible by name
        """
        response = self.client.get(reverse('show_last_users'))
        self.assertEqual(response.status_code, 200)

    def test_last_device_users_view_uses_correct_template(self):
        """
        Test that the device users view uses the correct template
        """
        response = self.client.get(reverse('show_last_users'))
        self.assertTemplateUsed(response,
                                'device_users/last_device_users.html')

    def test_last_device_users_context(self):
        """
        Test that the device users context is correct
        """
        response = self.client.get(reverse('show_last_users'))
        self.assertContains(response, 'Test FName 1')
        self.assertContains(response, 'Test LName 1')
        self.assertContains(response, 'UID_1')

    def test_all_device_users_url_exists_at_location(self):
        """
        Test that the device users url exists at the location
        """
        response = self.client.get('/product_user/all_users/')
        self.assertEqual(response.status_code, 200)

    def test_all_device_users_url_accessible_by_name(self):
        """
        Test that the device users url is accessible by name
        """
        response = self.client.get(reverse('show_all_users'))
        self.assertEqual(response.status_code, 200)

    def test_all_device_users_view_uses_correct_template(self):
        """
        Test that the device users view uses the correct template
        """
        response = self.client.get(reverse('show_all_users'))
        self.assertTemplateUsed(response,
                                'device_users/device_users.html')

    def test_all_device_users_context(self):
        """
        Test that the device users context is correct
        """
        response = self.client.get(reverse('show_all_users'))
        self.assertContains(response, 'Test FName 1')
        self.assertContains(response, 'Test LName 1')
        self.assertContains(response, 'UID_1')

    def test_show_user_info_url_exists_at_location(self):
        """
        Test that the device users url exists at the location
        """
        this_device_user = DeviceUser.objects.first()
        response = self.client.get(
            f"/product_user/user_info/{this_device_user.id}/")
        self.assertEqual(response.status_code, 200)

    def test_show_user_info_url_accessible_by_name(self):
        """
        Test that the device users url is accessible by name
        """
        this_device_user = DeviceUser.objects.first()
        response = self.client.get(
            reverse('show_user_info',
                    kwargs={'user_id': this_device_user.id})
        )
        self.assertEqual(response.status_code, 200)

    def test_show_user_info_view_uses_correct_template(self):
        """
        Test that the device users view uses the correct template
        """
        this_device_user = DeviceUser.objects.first()
        response = self.client.get(
            reverse('show_user_info',
                    kwargs={'user_id': this_device_user.id})
        )
        self.assertTemplateUsed(response,
                                'device_users/device_users_info.html')


class DeviceViewTestCase(TestCase):
    """
    Test cases for the device view
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

    def test_last_devices_url_exists_at_location(self):
        """
        Test that the last devices url exists at the location
        """
        response = self.client.get('/product_user/last_devices/')
        self.assertEqual(response.status_code, 200)

    def test_last_devices_url_accessible_by_name(self):
        """
        Test that the last devices url is accessible by name
        """
        response = self.client.get(reverse('show_last_devices'))
        self.assertEqual(response.status_code, 200)

    def test_last_devices_view_uses_correct_template(self):
        """
        Test that the last devices view uses the correct template
        """
        response = self.client.get(reverse('show_last_devices'))
        self.assertTemplateUsed(response,
                                'devices/last_devices.html')

    def test_last_devices_context(self):
        """
        Test that the last devices context is correct
        """
        response = self.client.get(reverse('show_last_devices'))
        self.assertEqual(response.context['devices'].count(), 10)

    def test_all_devices_url_exists_at_location(self):
        """
        Test that the all devices url exists at the location
        """
        response = self.client.get('/product_user/all_devices/')
        self.assertEqual(response.status_code, 200)

    def test_all_devices_url_accessible_by_name(self):
        """
        Test that the all devices url is accessible by name
        """
        response = self.client.get(reverse('show_all_devices'))
        self.assertEqual(response.status_code, 200)

    def test_all_devices_view_uses_correct_template(self):
        """
        Test that the all devices view uses the correct template
        """
        response = self.client.get(reverse('show_all_devices'))
        self.assertTemplateUsed(response,
                                'devices/all_devices.html')

    def test_all_devices_context(self):
        """
        Test that the all devices context is correct
        """
        response = self.client.get(reverse('show_all_devices'))
        self.assertEqual(response.context['devices'].count(), 20)

    def test_device_info_url_exists_at_location(self):
        """
        Test that the device info url exists at the location
        """
        this_device = Device.objects.first()
        response = self.client.get(
            f"/product_user/device_info/{this_device.id}/")
        self.assertEqual(response.status_code, 200)

    def test_device_info_url_accessible_by_name(self):
        """
        Test that the device info url is accessible by name
        """
        this_device = Device.objects.first()
        response = self.client.get(
            reverse('show_device_info',
                    kwargs={'device_id': this_device.id})
        )
        self.assertEqual(response.status_code, 200)

    def test_device_info_view_uses_correct_template(self):
        """
        Test that the device info view uses the correct template
        """
        this_device = Device.objects.first()
        response = self.client.get(
            reverse('show_device_info',
                    kwargs={'device_id': this_device.id})
        )
        self.assertTemplateUsed(response,
                                'devices/device_info.html')


class AddNewDeviceViewTestCase(TestCase):
    """
    Test cases for the add new device view
    """
    def setUp(self):
        # Create User object
        self.client = Client()
        self.username = 'test_user'
        self.password = 'test_password'
        self.user = tools.create_user_for_test(self.username, self.password)
        self.client.force_login(self.user)

        # Create device data for the tests
        Category.objects.create(name='Test Category')
        Brand.objects.create(name='Test Brand')
        CpuBrand.objects.create(name='Test CPU Brand')
        Entity.objects.create(name='Test Site')
        self.product = Product.objects.create(
            name='Test Product',
            category=Category.objects.get(name='Test Category'),
            brand=Brand.objects.get(name='Test Brand'),
        )
        self.cpu = Cpu.objects.create(
            name='Test CPU',
            cpu_brand=CpuBrand.objects.get(name='Test CPU Brand'),
        )
        self.location = Location.objects.create(
            name='Test',
            loc_number='12345',
            site=Entity.objects.get(name='Test Site'),
        )
        self.operating_system = OperatingSystem.objects.create(
            name='Test OS',
        )
        self.inventory_data = {
            'hostname': 'Test Hostname',
            'serial': 'Test012345',
            'cpu': self.cpu.id,
            'ram': '8',
            'addr_mac': '00:00:00:00:00:00',
            'storage': '480',
            'operating_system': self.operating_system.id,
        }
        self.immo_data = {
            'bc_number': '45000000',
            'inventory_number': '12345',
        }
        self.location_data = {
            'loc_name': self.location.id,
        }
        self.product_data = {
            'name': self.product.id,
        }

    @classmethod
    def tearDownClass(cls):
        # Call super to close connections and remove data from the database
        super().tearDownClass()
        # Delete the test database
        management.call_command('flush', verbosity=0, interactive=False)
        # Disconnect from the test database
        connections['default'].close()

    def test_add_new_device_url_exists_at_location(self):
        """
        Test that the add new device url exists at the location
        """
        response = self.client.get('/product_user/add_device/')
        self.assertEqual(response.status_code, 200)

    def test_add_new_device_url_accessible_by_name(self):
        """
        Test that the add new device url is accessible by name
        """
        response = self.client.get(reverse('add_new_device'))
        self.assertEqual(response.status_code, 200)

    def test_add_new_device_view_uses_correct_template(self):
        """
        Test that the add new device view uses the correct template
        """
        response = self.client.get(reverse('add_new_device'))
        self.assertTemplateUsed(response,
                                'devices/add_new_device.html')

    def test_add_new_device_form(self):
        """
        Test that the add new device form
        """
        response = self.client.post(
            reverse('add_new_device'), {
                'product_form': self.product_data,
                'inventory_form': self.inventory_data,
                'location_form': self.location_data,
                'immo_form': self.immo_data,
            }, follow=True
        )
        self.assertEqual(response.status_code, 200)
