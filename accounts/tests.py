from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import resolve, reverse

from allauth.account.forms import SignupForm
from allauth.account.views import SignupView


# Create your tests here.
# Tests end up testing the integration with allauth more than actual account app
class CustomUserTests(TestCase):
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            email="testuser68@email.com", username="testuser68", password="testpass123"
        )
        self.assertEqual(user.username, "testuser68")
        self.assertEqual(user.email, "testuser68@email.com")
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        User = get_user_model()
        user = User.objects.create_superuser(
            email="superuser@email.com", username="superuser", password="superpass123"
        )
        self.assertEqual(user.username, "superuser")
        self.assertEqual(user.email, "superuser@email.com")
        self.assertTrue(user.is_active)
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)


class SignupPageView(TestCase):
    def setUp(self):
        url = reverse("account_signup")
        self.response = self.client.get(url)

    def test_signup_template(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, "account/signup.html")
        self.assertContains(self.response, "Sign Up")
        self.assertNotContains(self.response, "I'm not on the page!?")

    def test_signup_form(self):
        form = self.response.context.get("form")
        self.assertIsInstance(form, SignupForm)
        self.assertContains(self.response, "csrfmiddlewaretoken")

    def test_signup_view(self):
        view = resolve("/accounts/signup/")
        self.assertEqual(view.func.__name__, SignupView.as_view().__name__)
