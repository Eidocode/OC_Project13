from django.core import mail
from django.test import TestCase
from django.urls import reverse
from django.core import management
from django.db import connections

from product.forms import ContactUsForm

import tools.func_for_tests as tools


class IndexViewTestCase(TestCase):
    """
    Test cases for the index view
    """
    @classmethod
    def setUpTestData(cls):
        # Create test data
        tools.create_tests_data()

    @classmethod
    def tearDownClass(cls):
        # Call super to close connections and remove data from the database
        super().tearDownClass()
        # Delete the test database
        management.call_command('flush', verbosity=0, interactive=False)
        # Disconnect from the test database
        connections['default'].close()

    def test_index_url_exists_at_location(self):
        """
        Test that the index url exists at the location
        """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_index_url_accessible_by_name(self):
        """
        Test that the index url is accessible by name
        """
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

    def test_index_view_uses_correct_template(self):
        """
        Test that the index view uses the correct template
        """
        response = self.client.get(reverse('index'))
        self.assertTemplateUsed(response, 'product/index.html')

    def test_index_view_uses_correct_context(self):
        """
        Test that the index view uses the correct context
        """
        response = self.client.get(reverse('index'))
        # Check that the context (types) is correct
        self.assertEqual(response.context['types']['Test_Category'], 20)
        # Check that the context (brands) is correct
        self.assertEqual(response.context['brands']['Test_Brand'], 20)
        # Check that the context (devices) returns the correct nb of devices
        self.assertEqual(response.context['devices'].count(), 5)


class ContactUsViewTestCase(TestCase):
    """
    Test cases for the contact us view
    """
    def test_contact_us_url_exists_at_location(self):
        """
        Test that the contact us url exists at the location
        """
        response = self.client.get('/product/contact_us/')
        self.assertEqual(response.status_code, 200)

    def test_contact_us_url_accessible_by_name(self):
        """
        Test that the contact us url is accessible by name
        """
        response = self.client.get(reverse('contact_us'))
        self.assertEqual(response.status_code, 200)

    def test_contact_us_view_uses_correct_template(self):
        """
        Test that the contact us view uses the correct template
        """
        response = self.client.get(reverse('contact_us'))
        self.assertTemplateUsed(response, 'product/contact_us/contact_us.html')

    def test_contact_us_view_contains_form(self):
        """
        Test that the contact us view contains the form
        """
        response = self.client.get(reverse('contact_us'))
        form = response.context['form']
        self.assertIsInstance(form, ContactUsForm)

    def test_contact_us_view_submission_success(self):
        """
        Test that the contact us view submission is successful
        """
        form_data = {
            'first_name': 'First_Name',
            'last_name': 'Last_Name',
            'email': 'email@test.com',
            'subject': 'Test_Subject',
            'message': 'Test_Message',
        }
        response = self.client.post(reverse('contact_us'), form_data)
        self.assertRedirects(response, reverse('contact_us'))
        self.assertEqual(len(mail.outbox), 1)

    def test_contact_us_view_submission_failure(self):
        """
        Test that the contact us view submission fails
        """
        form_data = {
            'first_name': '',
            'last_name': '',
            'email': '',
            'subject': '',
            'message': '',
        }
        response = self.client.post(reverse('contact_us'), form_data)
        self.assertEqual(len(mail.outbox), 0)
