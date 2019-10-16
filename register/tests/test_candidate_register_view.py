from django.test import TestCase
from django.urls import reverse
from register.views import register
from django.contrib.auth import get_user_model


class CandidateRegisterViewTest(TestCase):

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/register/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_is_accessible_by_name(self):
        response = self.client.get(reverse('register:register'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('register:register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'register/register.html')

    def test_form_passed_in_context(self):
        response = self.client.get(reverse('register:register'))
        self.assertTrue('form' in response.context)
