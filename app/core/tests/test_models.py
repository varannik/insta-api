from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        "Test creating a new user with an email is successful"

        email = 'varanik@gmail.com'
        password = '52041'

        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalize(self):
        """ Test the email for a new user is normalize """

        email = "varanik@GMAIL.COM"
        user = get_user_model().objects.create_user(email, '52041')
        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test Creating user with no email raises error"""

        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, '52041')

    def test_create_new_superuser(self):
        """Test Creating a new super user"""

        user = get_user_model().objects.create_superuser(
            email='varanik@gmail.com',
            password="52041"
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
