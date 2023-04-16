from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse

from product.models import DeviceUser, Device, Category, Brand, CpuBrand, \
    Product, Inventory, Cpu, Location, OperatingSystem, Entity


class DeviceUserViewTestCase(TestCase):
    """
    Test cases for the device user view
    """
    def setUp(self):
        # Create User object
        self.client = Client()
        self.username = 'test_user'
        self.email = 'test_email@test.com'
        self.password = 'test_password'
        self.first_name = 'Test_fname'
        self.last_name = 'Test_lname'
        self.user = User.objects.create_user(
            username=self.username,
            password=self.password,
            email=self.email,
            first_name=self.first_name,
            last_name=self.last_name,
            is_active=True
        )
        self.client.force_login(self.user)
        self.device_user1 = DeviceUser.objects.create(first_name='John',
                                                      last_name='Doe',
                                                      uid='12345')

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
        self.assertContains(response, self.device_user1.first_name)
        self.assertContains(response, self.device_user1.last_name)
        self.assertContains(response, self.device_user1.uid)

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
        self.assertContains(response, self.device_user1.first_name)
        self.assertContains(response, self.device_user1.last_name)
        self.assertContains(response, self.device_user1.uid)

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
        self.email = 'test_email@test.com'
        self.password = 'test_password'
        self.first_name = 'Test_fname'
        self.last_name = 'Test_lname'
        self.user = User.objects.create_user(
            username=self.username,
            password=self.password,
            email=self.email,
            first_name=self.first_name,
            last_name=self.last_name,
            is_active=True
        )
        self.client.force_login(self.user)

        # Create devices data
        Category.objects.create(name='Test Category')
        Brand.objects.create(name='Test Brand')
        CpuBrand.objects.create(name='Test CPU Brand')
        for i in range(20):
            Device.objects.create(
                product=Product.objects.create(
                    name=f'Product {i}',
                    category=Category.objects.get(name='Test Category'),
                    brand=Brand.objects.get(name='Test Brand'),
                ),
                device_user=DeviceUser.objects.create(
                    first_name=f'FName {i}',
                    last_name=f'LName {i}',
                    uid=f'UID {i}',
                ),
                inventory=Inventory.objects.create(
                    hostname=f'Hostname {i}',
                    serial=f'Serial Number {i}',
                    cpu=Cpu.objects.create(
                        name=f'CPU {i}',
                        cpu_brand=CpuBrand.objects.get(name='Test CPU Brand'),
                    )
                ),
            )

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
        self.email = 'test_email@test.com'
        self.password = 'test_password'
        self.first_name = 'Test_fname'
        self.last_name = 'Test_lname'
        self.user = User.objects.create_user(
            username=self.username,
            password=self.password,
            email=self.email,
            first_name=self.first_name,
            last_name=self.last_name,
            is_active=True
        )
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
