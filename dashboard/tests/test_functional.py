import time

from django.contrib.auth.models import User
from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from django.core import management
from django.db import connections

from product.models import Category, Brand, CpuBrand, OperatingSystem, Location, \
    Entity, Immo, Device, Product, DeviceUser, Inventory, Cpu


class DashboardFunctionalTest(LiveServerTestCase):
    """
    Functional test for the dashboard page
    """
    def setUp(self):
        """
        Set up the browser
        """
        self.browser = webdriver.Chrome()

        self.username = 'test_user'
        self.password = 'test_password'
        self.user = User.objects.create_user(
            username=self.username,
            password=self.password,
            email='test_email@test.com',
            first_name='Test_fname',
            last_name='Test_lname',
            is_active=True
        )

        # Create tests data
        Category.objects.create(name='Test_Category')
        Brand.objects.create(name='Test_Brand')
        CpuBrand.objects.create(name='Test_CPU_Brand')
        OperatingSystem.objects.create(name='Test_OS')
        Location.objects.create(
            name='Loc',
            loc_number=1234,
            site=Entity.objects.create(name='Test_Entity')
        )
        Immo.objects.create(
            bc_number='45000000',
            inventory_number='12345',
            location=Location.objects.get(
                name='Loc'
            ),
        )
        for i in range(20):
            Device.objects.create(
                product=Product.objects.create(
                    name=f'Test Product {i}',
                    category=Category.objects.get(name='Test_Category'),
                    brand=Brand.objects.get(name='Test_Brand'),
                ),
                device_user=DeviceUser.objects.create(
                    first_name=f'Test FName {i}',
                    last_name=f'Test LName {i}',
                    uid=f'UID_{i}',
                ),
                inventory=Inventory.objects.create(
                    hostname=f'Test Hostname {i}',
                    serial=f'Test Serial {i}',
                    cpu=Cpu.objects.create(
                        name=f'Test CPU {i}',
                        cpu_brand=CpuBrand.objects.get(name='Test_CPU_Brand'),
                    ),
                    operating_system=OperatingSystem.objects.get(
                        name='Test_OS'
                    ),
                ),
                immo=Immo.objects.get(
                    bc_number='45000000',
                )
            )

    def tearDown(self):
        """
        Close the browser
        """
        self.browser.quit()

    @classmethod
    def tearDownClass(cls):
        # Call super to close connections and remove data from the database
        super().tearDownClass()
        # Delete the test database
        management.call_command('flush', verbosity=0, interactive=False)
        # Disconnect from the test database
        connections['default'].close()

    def logUser(self):
        self.browser.get(self.live_server_url + '/users/login')
        time.sleep(5)

        username_input = self.browser.find_element(By.ID, 'id_username')
        username_input.send_keys(self.username)
        password_input = self.browser.find_element(By.ID, 'id_password')
        password_input.send_keys(self.password)
        submit_button = self.browser.find_element(By.ID, 'login_btn')
        submit_button.click()

    def test_dashboard_page(self):
        """
        Test the dashboard page
        """
        self.logUser()
        self.browser.get(self.live_server_url + '/dashboard/')
        time.sleep(5)




