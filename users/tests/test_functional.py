from django.contrib.auth.models import User
from django.test import LiveServerTestCase
from django.core import management
from django.db import connections
from django.urls import reverse
from selenium import webdriver
from selenium.webdriver.common.by import By

import tools.func_for_tests as tools


class UsersFunctionalTest(LiveServerTestCase):
    """
    Functional test for the users page when the user is not registered
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

    def test_links_between_pages(self):
        """
        Test the links between the pages
        """
        # Navigate to the homepage
        self.driver.get(self.live_server_url)
        # Navigate to the login page
        login_link = self.driver.find_element(By.LINK_TEXT, 'Cliquez ici')
        login_link.click()
        this_url = f"{self.live_server_url}{reverse('login')}"
        self.assertEqual(self.driver.current_url, this_url)
        # Return to the homepage
        self.driver.get(self.live_server_url)
        # Navigate to the logon page
        logon_link = self.driver.find_element(
            By.LINK_TEXT, "Première visite ? S'enregistrer")
        logon_link.click()
        this_url = f"{self.live_server_url}{reverse('signup')}"
        self.assertEqual(self.driver.current_url, this_url)
        # Navigate to the login page from the logon page
        login_link = self.driver.find_element(By.LINK_TEXT, 'Se connecter')
        login_link.click()
        this_url = f"{self.live_server_url}{reverse('login')}"
        self.assertEqual(self.driver.current_url, this_url)
        # Return to the logon page from the login page
        logon_link = self.driver.find_element(
            By.LINK_TEXT, "Première visite ? S'enregistrer")
        logon_link.click()
        this_url = f"{self.live_server_url}{reverse('signup')}"
        self.assertEqual(self.driver.current_url, this_url)

    def test_register_new_user(self):
        """
        Test the registration of a new user
        """
        # Count the number of registered users
        count_users = User.objects.count()
        # Navigate to the logon page
        self.driver.get(f"{self.live_server_url}{reverse('signup')}")
        # Fill the form
        self.driver.find_element(
            By.ID, 'id_username').send_keys('Testname')
        self.driver.find_element(
            By.ID, 'id_first_name').send_keys('First')
        self.driver.find_element(
            By.ID, 'id_last_name').send_keys('Last')
        self.driver.find_element(
            By.ID, 'id_email').send_keys('fl@test.fr')
        self.driver.find_element(
            By.ID, 'id_password1').send_keys('test_password')
        self.driver.find_element(
            By.ID, 'id_password2').send_keys('test_password')
        # Submit the form
        self.driver.find_element(
            By.ID, 'logon_btn').click()
        # Check that the user is registered
        self.assertEqual(User.objects.count(), count_users + 1)

    def test_login_user(self):
        """
        Test the login of a user
        """
        # Navigate to the login page
        self.driver.get(f"{self.live_server_url}{reverse('login')}")
        # Fill the form
        self.driver.find_element(
            By.ID, 'id_username').send_keys(self.username)
        self.driver.find_element(
            By.ID, 'id_password').send_keys(self.password)
        # Submit the form
        self.driver.find_element(
            By.ID, 'login_btn').click()
        # Check that the user is registered
        self.assertEqual(self.driver.current_url, f"{self.live_server_url}/")

    def test_user_account_information(self):
        """
        Test the user account information
        """
        # Navigate to the login page
        self.driver.get(f"{self.live_server_url}{reverse('login')}")
        # Log the user
        tools.log_user_for_functional_tests(
            self.username, self.password, self.driver)
        # Return to the homepage
        self.driver.get(self.live_server_url)
        # Navigate to the user account page
        user_nav = self.driver.find_element(By.ID, "navbarDropdown")
        user_nav.click()
        account_link = self.driver.find_element(By.LINK_TEXT,
                                                "Afficher le profil")
        account_link.click()
        self.assertEqual(self.driver.current_url,
                         f"{self.live_server_url}{reverse('account')}")

    def test_user_change_password(self):
        """
        Test the user change password
        """
        # Navigate to the login page
        self.driver.get(f"{self.live_server_url}{reverse('login')}")
        # Log the user
        tools.log_user_for_functional_tests(
            self.username, self.password, self.driver)
        # Navigate to the user account page
        self.driver.get(f"{self.live_server_url}{reverse('account')}")
        # Navigate to the change password page
        reset_pwd_btn = self.driver.find_element(By.ID, "reset_pwd_btn")
        reset_pwd_btn.click()
        # Fill the form
        self.driver.find_element(
            By.ID, 'id_old_password').send_keys(self.password)
        self.driver.find_element(
            By.ID, 'id_new_password1').send_keys('new_password')
        self.driver.find_element(
            By.ID, 'id_new_password2').send_keys('new_password')
        # Submit the form
        self.driver.find_element(By.ID, 'change_pwd_btn').click()
        # Check that the password has been changed
        self.assertEqual(self.driver.current_url,
                         f"{self.live_server_url}{reverse('account')}")

    def test_user_change_fullname(self):
        """
        Test the user change fullname
        """
        # Navigate to the login page
        self.driver.get(f"{self.live_server_url}{reverse('login')}")
        # Log the user
        tools.log_user_for_functional_tests(
            self.username, self.password, self.driver)
        # Navigate to the user account page
        self.driver.get(f"{self.live_server_url}{reverse('account')}")
        # Navigate to the change fullname page
        self.driver.find_element(By.ID, "change_fullname").click()
        # Fill the form
        self.driver.find_element(
            By.ID, 'id_first_name').send_keys('NewFirst')
        self.driver.find_element(
            By.ID, 'id_last_name').send_keys('NewLast')
        # Submit the form
        self.driver.find_element(By.ID, 'fullname_update_btn').click()
        # Check that the fullname has been changed
        self.assertEqual(self.driver.current_url,
                         f"{self.live_server_url}{reverse('account')}")

    def test_user_logout(self):
        """
        Test the user logout
        """
        # Navigate to the login page
        self.driver.get(f"{self.live_server_url}{reverse('login')}")
        # Log the user
        tools.log_user_for_functional_tests(
            self.username, self.password, self.driver)
        # Navigate to the user account page
        self.driver.get(f"{self.live_server_url}{reverse('account')}")
        # Logout the user
        self.driver.find_element(By.ID, "logout_btn").click()
        # Check that the user is logged out
        self.assertEqual(self.driver.current_url, f"{self.live_server_url}/")
