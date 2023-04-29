import re

from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.core import management
from django.db import connections
from django.test.client import Client
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.options import Options

import tools.func_for_tests as tools


def set_chrome_options():
    """
    Set Chrome options
    """
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument("window-size=1920,1080")
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--disable-gpu')
    return chrome_options


class DashboardFunctionalTest(StaticLiveServerTestCase):
    """
    Functional test for the dashboard page
    """
    def setUp(self):
        """
        Set up the browser
        """
        chrome_options = set_chrome_options()
        # Selenium webdriver
        self.driver = webdriver.Chrome(options=chrome_options)
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

    def test_dashboard_page_device_select(self):
        """
        Test the dashboard page with the device select
        """
        # Log the user
        self.driver.get(f"{self.live_server_url}/users/login")
        tools.log_user_for_functional_tests(
            self.username, self.password, self.driver)
        # Navigate to the dashboard
        self.driver.get(f"{self.live_server_url}/dashboard/")
        # Select device_select and change the selector
        device_input = Select(
            self.driver.find_element(By.ID, 'device-select'))
        device_input.select_by_visible_text('Test_Category')
        device_input.select_by_visible_text('All devices')
        self.assertEqual(
            self.driver.current_url, f"{self.live_server_url}/dashboard/")

    def test_dashboard_page_year_select(self):
        """
        Test the dashboard page with the year select
        """
        # Log the user
        self.driver.get(f"{self.live_server_url}/users/login")
        tools.log_user_for_functional_tests(
            self.username, self.password, self.driver)
        # Navigate to the dashboard
        self.driver.get(f"{self.live_server_url}/dashboard/")
        # Select year_select and change the selector
        year_input = Select(
            self.driver.find_element(By.ID, 'yearSelect'))
        year_input.select_by_visible_text('2022')
        year_input.select_by_visible_text('2023')
        self.assertEqual(
            self.driver.current_url, f"{self.live_server_url}/dashboard/")


class AdvancedSearchFunctionalTest(StaticLiveServerTestCase):
    """
    Functional test for the advanced search page
    """
    def setUp(self):
        """
        Set up the browser
        """
        chrome_options = set_chrome_options()
        # Selenium webdriver
        self.driver = webdriver.Chrome(options=chrome_options)
        # Django client
        self.client = Client()
        # Set username and password for the test
        self.username = 'test_user'
        self.password = 'test_password'
        # Create the tests data
        tools.create_tests_data()
        # Create the user
        tools.create_user_for_test(self.username, self.password)
        # Log the user
        self.driver.get(f"{self.live_server_url}/users/login")
        tools.log_user_for_functional_tests(
            self.username, self.password, self.driver)

    def tearDown(self):
        """
        Close the browser
        """
        self.driver.quit()

    @classmethod
    def tearDownClass(cls):
        """
        Call super to close connections and remove data from the database
        """
        # Call super to close connections and remove data from the database
        super().tearDownClass()
        # Delete the test database
        management.call_command('flush', verbosity=0, interactive=False)
        # Disconnect from the test database
        connections['default'].close()

    def test_advanced_search_by_device(self):
        """
        Test the advanced search page by device name
        """
        # Navigate to the advanced search page
        self.driver.get(f"{self.live_server_url}/dashboard/advanced_search/")
        # Search by Device
        search_input = self.driver.find_element(By.ID, 'id_search')
        search_input.send_keys('hostname')
        submit_button = self.driver.find_element(By.ID, 'send_btn')
        submit_button.click()
        this_url = f"{self.live_server_url}/dashboard/advanced_search/" \
                   f"?search_filter=device&search=hostname&brand_filter=All&" \
                   f"type_filter=All&radio_device_user=All_users"
        current_url_without_token = re.sub(
            r'csrfmiddlewaretoken=[^&]*&?', '', self.driver.current_url)
        self.assertEqual(current_url_without_token, this_url)

    def test_advanced_search_by_entity(self):
        """
        Test the advanced search page by entity name
        """
        # Navigate to the advanced search page
        self.driver.get(f"{self.live_server_url}/dashboard/advanced_search/")
        # Search by Entity
        filter_select = Select(
            self.driver.find_element(By.ID, 'id_search_filter'))
        filter_select.select_by_visible_text('Entité')
        search_input = self.driver.find_element(By.ID, 'id_search')
        search_input.send_keys('entity')
        submit_button = self.driver.find_element(By.ID, 'send_btn')
        submit_button.click()
        this_url = f"{self.live_server_url}/dashboard/advanced_search/" \
                   f"?search_filter=entity&search=entity&brand_filter=All&" \
                   f"type_filter=All&radio_device_user=All_users"
        current_url_without_token = re.sub(
            r'csrfmiddlewaretoken=[^&]*&?', '', self.driver.current_url)
        self.assertEqual(current_url_without_token, this_url)

    def test_advanced_search_by_user(self):
        """
        Test the advanced search page by user
        """
        # Navigate to the advanced search page
        self.driver.get(f"{self.live_server_url}/dashboard/advanced_search/")
        # Search by User
        filter_select = Select(
            self.driver.find_element(By.ID, 'id_search_filter'))
        filter_select.select_by_visible_text('Utilisateur')
        search_input = self.driver.find_element(By.ID, 'id_search')
        search_input.send_keys('fname')
        submit_button = self.driver.find_element(By.ID, 'send_btn')
        submit_button.click()
        this_url = f"{self.live_server_url}/dashboard/advanced_search/" \
                   f"?search_filter=user&search=fname&brand_filter=All&" \
                   f"type_filter=All&radio_device_user=All_users"
        current_url_without_token = re.sub(
            r'csrfmiddlewaretoken=[^&]*&?', '', self.driver.current_url)
        self.assertEqual(current_url_without_token, this_url)

    def test_advanced_search_by_brand(self):
        """
        Test the advanced search page by brand
        """
        # Navigate to the advanced search page
        self.driver.get(f"{self.live_server_url}/dashboard/advanced_search/")
        # Search with brand_filter
        brand_filter_select = Select(
            self.driver.find_element(By.ID, 'brand_filter'))
        brand_filter_select.select_by_visible_text('Test_Brand')
        filter_select = Select(
            self.driver.find_element(By.ID, 'id_search_filter'))
        filter_select.select_by_visible_text('Périphérique')
        search_input = self.driver.find_element(By.ID, 'id_search')
        search_input.send_keys('hostname')
        submit_button = self.driver.find_element(By.ID, 'send_btn')
        submit_button.click()
        this_url = f"{self.live_server_url}/dashboard/advanced_search/" \
                   f"?search_filter=device&search=hostname&" \
                   f"brand_filter=Test_Brand&type_filter=All&" \
                   f"radio_device_user=All_users"
        current_url_without_token = re.sub(
            r'csrfmiddlewaretoken=[^&]*&?', '', self.driver.current_url)
        self.assertEqual(current_url_without_token, this_url)

    def test_advanced_search_by_type(self):
        """
        Test the advanced search page by type
        """
        # Navigate to the advanced search page
        self.driver.get(f"{self.live_server_url}/dashboard/advanced_search/")
        # Search with type_filter
        type_filter_select = Select(
            self.driver.find_element(By.ID, 'type_filter'))
        type_filter_select.select_by_visible_text('Test_Category')
        search_input = self.driver.find_element(By.ID, 'id_search')
        search_input.send_keys('serial')
        submit_button = self.driver.find_element(By.ID, 'send_btn')
        submit_button.click()
        this_url = f"{self.live_server_url}/dashboard/advanced_search/" \
                   f"?search_filter=device&search=serial&" \
                   f"brand_filter=All&type_filter=Test_Category&" \
                   f"radio_device_user=All_users"
        current_url_without_token = re.sub(
            r'csrfmiddlewaretoken=[^&]*&?', '', self.driver.current_url)
        self.assertEqual(current_url_without_token, this_url)

    def test_advanced_search_by_radio_device_user(self):
        """
        Test the advanced search page by radio device user
        """
        # Navigate to the advanced search page
        self.driver.get(f"{self.live_server_url}/dashboard/advanced_search/")
        # Search with radio_device_user
        without_user_button = self.driver.find_element(
            By.ID, 'device_without_user_checkbox')
        without_user_button.click()
        search_input = self.driver.find_element(By.ID, 'id_search')
        search_input.send_keys('test')
        submit_button = self.driver.find_element(By.ID, 'send_btn')
        submit_button.click()
        this_url = f"{self.live_server_url}/dashboard/advanced_search/" \
                   f"?search_filter=device&search=test&" \
                   f"brand_filter=All&type_filter=All&" \
                   f"radio_device_user=Without"
        current_url_without_token = re.sub(
            r'csrfmiddlewaretoken=[^&]*&?', '', self.driver.current_url)
        self.assertEqual(current_url_without_token, this_url)
