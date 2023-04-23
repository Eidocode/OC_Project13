import time

from django.test import LiveServerTestCase
from django.urls import reverse
from django.core import management
from django.db import connections
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.options import Options

from product.models import Device

import tools.func_for_tests as tools


class AddNewDeviceFunctionalTest(LiveServerTestCase):
    """
    Functional test for the add new device page
    """
    def setUp(self):
        """
        Set up the browser
        """
        # Selenium webdriver
        self.driver = webdriver.Chrome()
        # Set username and password for the test
        self.username = 'test_user'
        self.password = 'test_password'
        # Create the tests data
        tools.create_tests_data()
        # Create the user
        tools.create_user_for_test(self.username, self.password)

    def tearDown(self):
        """
        Close the browser
        """
        self.driver.quit()

    @classmethod
    def tearDownClass(cls):
        # Call super to close connections and remove data from the database
        super().tearDownClass()
        # Delete the test database
        management.call_command('flush', verbosity=0, interactive=False)
        # Disconnect from the test database
        connections['default'].close()

    def test_add_new_device(self):
        """
        Test that the add new device form works and adds a new device
        """
        # Log the user
        self.driver.get(f"{self.live_server_url}/users/login")
        tools.log_user_for_functional_tests(
            self.username, self.password, self.driver)

        # Log in and navigate to the add new device page
        self.driver.get(f"{self.live_server_url}/product_user/add_device/")

        # Fills out the product form
        hostname_input = self.driver.find_element(By.NAME, "hostname")
        hostname_input.send_keys('Test_Hostname')
        product_select = Select(self.driver.find_element(By.ID, 'id_name'))
        product_select.select_by_value("1")
        serial_input = self.driver.find_element(By.ID, "id_serial")
        serial_input.send_keys("Test012345")
        addr_mac_input = self.driver.find_element(By.ID, "id_addr_mac")
        addr_mac_input.send_keys("00:00:00:00:00:00")
        cpu_select = Select(self.driver.find_element(By.ID, "id_cpu"))
        cpu_select.select_by_value("1")
        ram_input = self.driver.find_element(By.ID, "id_ram")
        ram_input.send_keys("8")
        storage_input = self.driver.find_element(By.ID, "id_storage")
        storage_input.send_keys("480")
        os_select = Select(self.driver.find_element(By.ID,
                                                    "id_operating_system"))
        os_select.select_by_value("1")
        bc_input = self.driver.find_element(By.ID, "id_bc_number")
        bc_input.send_keys("12345")
        inventory_input = self.driver.find_element(By.ID,
                                                   "id_inventory_number")
        inventory_input.send_keys("55555")
        location_select = Select(self.driver.find_element(By.ID,
                                                          "id_loc_name"))
        location_select.select_by_value("1")
        submit_device = self.driver.find_element(By.ID, 'add_new_device_btn')
        submit_device.click()

        # Check that the device was added
        self.assertEqual(Device.objects.count(), 21)
        # Check if the user is redirected to the home page
        self.assertEqual(self.driver.current_url,
                         f"{self.live_server_url}{reverse('show_all_devices')}")


class DeviceInformationPageTest(LiveServerTestCase):
    """
    Functional test for the device information page
    """
    def setUp(self):
        """
        Set up the browser
        """
        # Selenium webdriver
        self.driver = webdriver.Chrome()
        # Set username and password for the test
        self.username = 'test_user'
        self.password = 'test_password'
        # Create the tests data
        tools.create_tests_data()
        # Create the user
        tools.create_user_for_test(self.username, self.password)

    def tearDown(self):
        """
        Close the browser
        """
        self.driver.quit()

    @classmethod
    def tearDownClass(cls):
        # Call super to close connections and remove data from the database
        super().tearDownClass()
        # Delete the test database
        management.call_command('flush', verbosity=0, interactive=False)
        # Disconnect from the test database
        connections['default'].close()

    def test_device_information_page(self):
        """
        Test the device information page
        """
        # Log the user
        self.driver.get(f"{self.live_server_url}{reverse('login')}")
        tools.log_user_for_functional_tests(
            self.username, self.password, self.driver)
        # Navigate to the all devices page
        self.driver.get(f"{self.live_server_url}{reverse('show_all_devices')}")
        # Navigate to the device information page
        details_btn = self.driver.find_element(By.ID, 'more_details')
        details_btn.click()
        self.assertIn(f"{self.live_server_url}/product_user/device_info/",
                      self.driver.current_url)
        # Navigate to the linked user page
        linked_user = self.driver.find_element(By.ID, 'user_detail')
        linked_user.click()
        self.assertIn(f"{self.live_server_url}/product_user/user_info/",
                      self.driver.current_url)


class DeviceUserInformationPageTest(LiveServerTestCase):
    """
    Functional test for the device_user information page
    """
    def setUp(self):
        """
        Set up the browser
        """
        # Add the following lines to set Chrome options
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        # Selenium webdriver
        self.driver = webdriver.Chrome()
        # Set username and password for the test
        self.username = 'test_user'
        self.password = 'test_password'
        # Create the tests data
        tools.create_tests_data()
        # Create the user
        tools.create_user_for_test(self.username, self.password)

    def tearDown(self):
        """
        Close the browser
        """
        self.driver.quit()

    @classmethod
    def tearDownClass(cls):
        # Call super to close connections and remove data from the database
        super().tearDownClass()
        # Delete the test database
        management.call_command('flush', verbosity=0, interactive=False)
        # Disconnect from the test database
        connections['default'].close()

    def test_device_information_page(self):
        """
        Test the device_user information page
        """
        # Log the user
        self.driver.get(f"{self.live_server_url}{reverse('login')}")
        tools.log_user_for_functional_tests(
            self.username, self.password, self.driver)
        # Navigate to the all device_users page
        self.driver.get(f"{self.live_server_url}{reverse('show_all_users')}")
        # Navigate to the device information page
        btn_detail = self.driver.find_element(By.ID, 'more_details')
        btn_detail.click()
        self.assertIn(f"{self.live_server_url}/product_user/user_info/",
                      self.driver.current_url)
        # Navigate to the linked user page
        linked_user = self.driver.find_element(By.ID, 'device_detail')
        linked_user.click()
        self.assertIn(f"{self.live_server_url}/product_user/device_info/",
                      self.driver.current_url)
