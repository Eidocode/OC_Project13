from django.test import TestCase
from django.urls import reverse


class IndexPageTestCase(TestCase):
    """
    Tests for the index page.
    """

    def test_index_url_exists_at_location(self):
        """
        Checks that the index page is accessible at /
        """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_index_url_by_name(self):
        """
        Checks that the index page is accessible with name "index"
        """
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

    def test_index_url_uses_correct_template(self):
        """
        Checks that the index page uses the correct template
        """
        response = self.client.get(reverse('index'))
        self.assertTemplateUsed(response, 'product/index.html')
