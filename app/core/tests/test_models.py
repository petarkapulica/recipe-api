from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_success(self):
        email = 'test@test.com'
        password = 'secret123'
        user = get_user_model().objects.create_user(email, password)

        self.assertEqual('test@test.com', user.email)
        self.assertTrue(user.check_password(password))

    def test_create_user_with_normalized_email(self):
        email = 'test@TEST.COM'
        user = get_user_model().objects.create_user(email)

        self.assertEqual('test@test.com', user.email)

    def test_create_user_with_empty_email(self):
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test123')

    def test_create_superuser(self):
        email = 'test@test.com'
        password = 'secret123'
        user = get_user_model().objects.create_superuser(email, password)

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
