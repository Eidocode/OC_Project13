import time

from django.contrib.auth.models import User
from django.test import LiveServerTestCase, Client
from django.urls import reverse
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from product.models import Category, Brand, CpuBrand, Entity, Product, Cpu, \
    Location, OperatingSystem, Device

# Set the path to the chromedriver
# chrome_driver_path = "C:\webdriver\chromedriver.exe"


class AddNewDeviceFunctionalTest(LiveServerTestCase):
    """
    Functional test for the add new device page
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

    def logUser(self):
        self.browser.get(self.live_server_url + '/users/login')
        username_input = self.browser.find_element(By.ID, 'id_username')
        username_input.send_keys(self.username)
        password_input = self.browser.find_element(By.ID, 'id_password')
        password_input.send_keys(self.password)
        submit_button = self.browser.find_element(By.ID, 'login_btn')
        submit_button.click()

    def tearDown(self):
        """
        Close the browser
        """
        self.browser.quit()

    def test_add_new_device(self):
        """
        Test that the add new device form works and adds a new device
        """
        # Log in and navigate to the add new device page
        self.logUser()
        self.browser.get(self.live_server_url + '/product_user/add_device/')

        # Fills out the product form
        hostname_input = self.browser.find_element(By.NAME,
                                                       "hostname")
        hostname_input.send_keys('Test_Hostname')
        product_select = Select(
            self.browser.find_element(By.ID, 'id_name'))
        product_select.select_by_value("1")
        serial_input = self.browser.find_element(By.ID, "id_serial")
        serial_input.send_keys("Test012345")
        addr_mac_input = self.browser.find_element(By.ID, "id_addr_mac")
        addr_mac_input.send_keys("00:00:00:00:00:00")
        cpu_select = Select(
            self.browser.find_element(By.ID, "id_cpu"))
        cpu_select.select_by_value("1")
        ram_input = self.browser.find_element(By.ID, "id_ram")
        ram_input.send_keys("8")
        storage_input = self.browser.find_element(By.ID, "id_storage")
        storage_input.send_keys("480")
        os_select = Select(
            self.browser.find_element(By.ID, "id_operating_system"))
        os_select.select_by_value("1")
        bc_input = self.browser.find_element(By.ID, "id_bc_number")
        bc_input.send_keys("12345")
        inventory_input = self.browser.find_element(By.ID,
                                                    "id_inventory_number")
        inventory_input.send_keys("55555")
        location_select = Select(
            self.browser.find_element(By.ID, "id_loc_name"))
        location_select.select_by_value("1")
        submit_device = self.browser.find_element(By.ID, 'add_new_device_btn')
        submit_device.click()

        # Check that the device was added
        self.assertEqual(Device.objects.count(), 1)

        # Check if the user is redirected to the home page
        self.assertEqual(self.browser.current_url,
                         self.live_server_url + reverse('show_all_devices'))





