from django.contrib.auth.hashers import check_password
from django.core import mail, management
from django.test import TestCase, Client
from django.db import connections

from django.contrib.auth.models import User
from django.urls import reverse


class LoginViewTestCase(TestCase):
    """
    Test cases for the login view
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

    @classmethod
    def tearDownClass(cls):
        # Call super to close connections and remove data from the database
        super().tearDownClass()
        # Delete the test database
        management.call_command('flush', verbosity=0, interactive=False)
        # Disconnect from the test database
        connections['default'].close()

    def test_login_url_exists_at_location(self):
        """
        Test that the login url exists at the location
        """
        response = self.client.get('/users/login/')
        self.assertEqual(response.status_code, 200)

    def test_login_url_accessible_by_name(self):
        """
        Test that the login url is accessible by name
        """
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)

    def test_login_view_uses_correct_template(self):
        """
        Test that the login view uses the correct template
        """
        response = self.client.get(reverse('login'))
        self.assertTemplateUsed(response, 'registration/login.html')

    def test_login_success(self):
        """
        Test that the user can log in successfully
        """
        response = self.client.post(
            reverse('login'),
            {'username': self.username, 'password': self.password}
        )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('index'))

    def test_login_failure(self):
        """
        Test that a user cannot log in with incorrect credentials
        """
        response = self.client.post(
            reverse('login'),
            {'username': 'bad_username', 'password': 'bad_password'}
        )
        self.assertEqual(response.status_code, 200)


class SignupViewTestCase(TestCase):
    """
    Test cases for the signup view
    """
    def test_signup_url_exists_at_location(self):
        """
        Test that the signup url exists at the location
        """
        response = self.client.get('/users/signup/')
        self.assertEqual(response.status_code, 200)

    def test_signup_url_accessible_by_name(self):
        """
        Test that the signup url is accessible by name
        """
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)

    def test_signup_view_uses_correct_template(self):
        """
        Test that the signup view uses the correct template
        """
        response = self.client.get(reverse('signup'))
        self.assertTemplateUsed(response, 'registration/signup.html')

    def test_signup_success(self):
        """
        Test that the user can sign up successfully
        """
        response = self.client.post(reverse('signup'), {
            'username': 'testuser',
            'first_name': 'Test_fname',
            'last_name': 'Test_lname',
            'email': 'test_email@test.com',
            'password1': 'testpassword',
            'password2': 'testpassword'
        })

        # Check form validity
        form = response.context.get('form')
        self.assertTrue(form.is_valid())

        # Test that the user was created
        self.assertEqual(User.objects.count(), 1)
        user = User.objects.first()
        self.assertEqual(user.username, 'testuser')
        self.assertEqual(user.email, 'test_email@test.com')
        self.assertFalse(user.is_active)

        # Test email activation send
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].subject,
                         '[NO-REPLY] Activer votre compte OC-Inventory')

    def test_signup_failure(self):
        """
        Test user sign up with invalid data
        """
        response = self.client.post(reverse('signup'), {
            'username': '',
            'first_name': '',
            'last_name': '',
            'email': 'invalidemail',
            'password1': 'testpasswd',
            'password2': 'testpassword'
        })

        # Check user was not created
        form = response.context.get('form')
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 5)

        # Test user not created
        self.assertEqual(User.objects.count(), 0)


class AccountViewTestCase(TestCase):
    """
    Test cases for the account view
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
        self.client.login(username=self.username, password=self.password)

    @classmethod
    def tearDownClass(cls):
        # Call super to close connections and remove data from the database
        super().tearDownClass()
        # Delete the test database
        management.call_command('flush', verbosity=0, interactive=False)
        # Disconnect from the test database
        connections['default'].close()

    def test_account_url_exists_at_location(self):
        """
        Test that the account url exists at the location
        """
        response = self.client.get('/users/account/')
        self.assertEqual(response.status_code, 200)

    def test_account_url_accessible_by_name(self):
        """
        Test that the account url is accessible by name
        """
        response = self.client.get(reverse('account'))
        self.assertEqual(response.status_code, 200)

    def test_account_view_uses_correct_template(self):
        """
        Test that the account view uses the correct template
        """
        response = self.client.get(reverse('account'))
        self.assertTemplateUsed(response, 'users/account/account.html')


class FullnameChangeViewTestCase(TestCase):
    """
    Test cases for the Fullname change view
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
        self.client.login(username=self.username, password=self.password)

    @classmethod
    def tearDownClass(cls):
        # Call super to close connections and remove data from the database
        super().tearDownClass()
        # Delete the test database
        management.call_command('flush', verbosity=0, interactive=False)
        # Disconnect from the test database
        connections['default'].close()

    def test_fullname_change_url_exists_at_location(self):
        """
        Test that the fullname change url exists at the location
        """
        response = self.client.get('/users/change_flname/')
        self.assertEqual(response.status_code, 200)

    def test_fullname_change_url_accessible_by_name(self):
        """
        Test that the fullname change url is accessible by name
        """
        response = self.client.get(reverse('change_fullname'))
        self.assertEqual(response.status_code, 200)

    def test_fullname_change_view_uses_correct_template(self):
        """
        Test that the fullname change view uses the correct template
        """
        response = self.client.get(reverse('change_fullname'))
        self.assertTemplateUsed(response, 'users/account/change_fullname.html')

    def test_fullname_change_success(self):
        """
        Test that the user can change their fullname successfully
        """
        response = self.client.post(reverse('change_fullname'), {
            'first_name': 'New_fname',
            'last_name': 'New_lname'
        })
        self.assertEqual(response.status_code, 302)
        # Reload the user from the database to get the latest changes
        self.user.refresh_from_db()
        self.assertEqual(self.user.first_name, 'New_fname')
        self.assertEqual(self.user.last_name, 'New_lname')

    def test_fullname_change_failure(self):
        """
        Test that the user cannot change their fullname successfully
        """
        response = self.client.post(reverse('change_fullname'), {
            'first_name': 'New_fname',
            'last_name': ''
        })
        self.assertEqual(response.status_code, 200)
        self.assertFormError(response, 'form', 'last_name',
                             'Ce champ est obligatoire.')


class PasswordChangeViewTestCase(TestCase):
    """
    Test cases for the password change view
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
        self.client.login(username=self.username, password=self.password)

    @classmethod
    def tearDownClass(cls):
        # Call super to close connections and remove data from the database
        super().tearDownClass()
        # Delete the test database
        management.call_command('flush', verbosity=0, interactive=False)
        # Disconnect from the test database
        connections['default'].close()
    def test_password_change_url_exists_at_location(self):
        """
        Test that the password change url exists at the location
        """
        response = self.client.get('/users/change_pwd/')
        self.assertEqual(response.status_code, 200)

    def test_password_change_url_accessible_by_name(self):
        """
        Test that the password change url is accessible by name
        """
        response = self.client.get(reverse('change_password'))
        self.assertEqual(response.status_code, 200)

    def test_password_change_view_uses_correct_template(self):
        """
        Test that the password change view uses the correct template
        """
        response = self.client.get(reverse('change_password'))
        self.assertTemplateUsed(response, 'users/account/change_password.html')

    def test_password_change_success(self):
        """
        Test that the user can change their password successfully
        """
        response = self.client.post(reverse('change_password'), {
            'old_password': 'test_password',
            'new_password1': 'new_password',
            'new_password2': 'new_password'
        })
        self.assertEqual(response.status_code, 302)
        # Reload the user from the database to get the latest changes
        self.user.refresh_from_db()
        self.assertTrue(check_password('new_password', self.user.password))
