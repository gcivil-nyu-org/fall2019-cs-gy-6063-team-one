from django.test import TestCase

from register.forms import CandidateRegistrationForm


class CandidateRegistrationFormTest(TestCase):

    def test_first_name_field_label(self):
        form = CandidateRegistrationForm()
        self.assertTrue(form.fields['first_name'].label == 'First Name')

    def test_last_name_field_label(self):
        form = CandidateRegistrationForm()
        self.assertTrue(form.fields['last_name'].label == 'Last Name')

    def test_email_field_label(self):
        form = CandidateRegistrationForm()
        self.assertTrue(form.fields['email'].label == 'Email')

    def test_everything_correct(self):
        form = CandidateRegistrationForm(data={'first_name': 'James', 'last_name': 'Tan', 'email': 'jamestan@gmail.com',
                                               'password1': 'Saddog123!', 'password2': 'Saddog123!'})
        self.assertTrue(form.is_valid())

    def test_first_name_missing(self):
        form = CandidateRegistrationForm(data={'first_name': '', 'last_name': 'Tan', 'email': 'jamestan@gmail.com',
                                               'password1': 'Saddog123!', 'password2': 'Saddog123!'})
        self.assertFalse(form.is_valid())

    def test_last_name_missing(self):
        form = CandidateRegistrationForm(data={'first_name': 'James', 'last_name': '', 'email': 'jamestan@gmail.com',
                                               'password1': 'Saddog123!', 'password2': 'Saddog123!'})
        self.assertFalse(form.is_valid())

    def test_email_missing(self):
        form = CandidateRegistrationForm(data={'first_name': 'James', 'last_name': 'Tan', 'email': '',
                                               'password1': 'Saddog123!', 'password2': 'Saddog123!'})
        self.assertFalse(form.is_valid())

    def test_password1_missing(self):
        form = CandidateRegistrationForm(data={'first_name': 'James', 'last_name': 'Tan', 'email': 'jamestan@gmail.com',
                                               'password1': '', 'password2': 'Saddog123!'})
        self.assertFalse(form.is_valid())

    def test_password2_missing(self):
        form = CandidateRegistrationForm(data={'first_name': 'James', 'last_name': 'Tan', 'email': 'jamestan@gmail.com',
                                               'password1': 'Saddog123!', 'password2': ''})
        self.assertFalse(form.is_valid())

    def test_password2_mismatch(self):
        form = CandidateRegistrationForm(data={'first_name': 'James', 'last_name': 'Tan', 'email': 'jamestan@gmail.com',
                                               'password1': 'Saddog123!', 'password2': 'Saddog123'})
        self.assertFalse(form.is_valid())

    def test_first_name_symbols(self):
        form = CandidateRegistrationForm(data={'first_name': '*&^^', 'last_name': 'Tan', 'email': 'jamestan@gmail.com',
                                               'password1': 'Saddog123!', 'password2': 'Saddog123!'})
        self.assertFalse(form.is_valid())

    def test_first_name_numbers(self):
        form = CandidateRegistrationForm(data={'first_name': '123', 'last_name': 'Tan', 'email': 'jamestan@gmail.com',
                                               'password1': 'Saddog123!', 'password2': 'Saddog123!'})
        self.assertFalse(form.is_valid())

    def test_last_name_symbols(self):
        form = CandidateRegistrationForm(data={'first_name': 'James', 'last_name': '*&^^', 'email': 'jamestan@gmail.com',
                                               'password1': 'Saddog123!', 'password2': 'Saddog123!'})
        self.assertFalse(form.is_valid())

    def test_last_name_numbers(self):
        form = CandidateRegistrationForm(data={'first_name': 'James', 'last_name': '123', 'email': 'jamestan@gmail.com',
                                               'password1': 'Saddog123!', 'password2': 'Saddog123!'})
        self.assertFalse(form.is_valid())
