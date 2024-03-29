from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


# Set Chrome options
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


class IndexFunctionalTest(StaticLiveServerTestCase):
    """
    Functional test for the index page
    """
    def setUp(self):
        """
        Set up the browser
        """
        chrome_options = set_chrome_options()
        # Selenium webdriver
        self.driver = webdriver.Chrome(options=chrome_options)

    def tearDown(self):
        """
        Close the browser
        """
        self.driver.quit()

    def test_browser_title_display(self):
        """
        Test the browser title
        """
        self.driver.get(self.live_server_url)
        self.assertIn("OC-Inventory Home", self.driver.title)

    def test_index_page_loads_without_user_account(self):
        """
        Test the index page loads without a connected user
        """
        self.driver.get(self.live_server_url)
        warning_text = self.driver.find_element(By.CLASS_NAME, 'text-danger')
        self.assertIn(
            "Vous devez être connecté pour utiliser cette application !",
            warning_text.text
        )
        login_link = self.driver.find_element(By.LINK_TEXT, 'Cliquez ici')
        login_link.click()
        self.assertEqual(self.driver.current_url,
                         self.live_server_url + '/users/login/')
        self.driver.get(self.live_server_url)
        reg_link = self.driver.find_element(By.LINK_TEXT,
                                             "Première visite ? S'enregistrer")
        reg_link.click()
        self.assertEqual(self.driver.current_url,
                         self.live_server_url + '/users/signup/')


class ContactUsFunctionalTest(StaticLiveServerTestCase):
    """
    Functional test for the contact us page
    """
    def setUp(self):
        """
        Set up the browser
        """
        chrome_options = set_chrome_options()
        # Selenium webdriver
        self.driver = webdriver.Chrome(options=chrome_options)

    def tearDown(self):
        """
        Close the browser
        """
        self.driver.quit()

    def test_contact_us_form_success(self):
        """
        Test the contact us form (success)
        """
        self.driver.get(self.live_server_url + '/product/contact_us/')

        # Fill the form
        f_name = self.driver.find_element('name', 'first_name')
        f_name.send_keys('Test_fname')
        l_name = self.driver.find_element('name', 'last_name')
        l_name.send_keys('Test_lname')
        email = self.driver.find_element('name', 'email')
        email.send_keys('test_email@email.com')
        subject = self.driver.find_element('name', 'subject')
        subject.send_keys('Test_subject')
        message = self.driver.find_element('name', 'message')
        message.send_keys('Test_message')

        # Submit the form
        submit = self.driver.find_element('id', 'contact_us_btn')
        submit.click()

        # Stay on the contactus page with a success message
        self.assertEqual(self.driver.current_url,
                         self.live_server_url + '/product/contact_us/')
        success_message = self.driver.find_element(By.CLASS_NAME,
                                                    'alert-success')
        self.assertTrue(success_message.is_displayed())
