from django.test import TestCase
from django.contrib.auth import get_user_model


class UsersManagersTests(TestCase):
    """TestCase for User Model."""
    def test_create_user(self):
        """Test user creation"""
        User = get_user_model()
        user = User.objects.create_user(email="user@gmail.com", password="_12User")
        self.assertEqual(user.email, "user@gmail.com")
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        try:
            # username is None for the AbstractUser option
            # username does not exist for the AbstractBaseUser option
            self.assertIsNone(user.username)
        except AttributeError:
            pass
        with self.assertRaises(TypeError):
            User.objects.create_user()
        with self.assertRaises(TypeError):
            User.objects.create_user(email="")
        with self.assertRaises(ValueError):
            User.objects.create_user(email="", password="_12User")

    def test_create_superuser(self):
        """Test superuser creation."""
        User = get_user_model()
        admin_user = User.objects.create_superuser(email="super_user@gmail.com", password="@1Super")
        self.assertEqual(admin_user.email, "super_user@gmail.com")
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)
        try:
            # username is None for the AbstractUser option
            # username does not exist for the AbstractBaseUser option
            self.assertIsNone(admin_user.username)
        except AttributeError:
            pass
        with self.assertRaises(ValueError):
            User.objects.create_superuser(
                email="super_user@gmail.com", password="@1Super", is_superuser=False)
