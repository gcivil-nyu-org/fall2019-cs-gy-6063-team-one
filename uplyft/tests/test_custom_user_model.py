from django.test import TestCase
from uplyft.models import CustomUser


class CustomUserModelTest(TestCase):
    first_name_max_length = 30
    last_name_max_length = 150
    email_max_length = 200
    password_max_length = 128
    first_name = "Bob"
    last_name = "Smith"
    email = "bobsmith@gmail.com"
    password = "Specialpassword123"

    @classmethod
    def setUpTestData(cls):
        CustomUser.objects.create_user(
            email=cls.email,
            password=cls.password,
            first_name=cls.first_name,
            last_name=cls.last_name
        )

    def test_first_name_label(self):
        user = CustomUser.objects.get(id=1)
        field_label = user._meta.get_field('first_name').verbose_name
        self.assertEquals(field_label, 'first name')

    def test_fullname_correct(self):
        user = CustomUser.objects.get(id=1)
        name = user.get_full_name()
        self.assertEquals(name, 'Bob Smith')

    def test_short_name(self):
        user = CustomUser.objects.get(id=1)
        name = user.get_short_name()
        self.assertEquals(name, self.first_name)

    def test_check_password(self):
        user = CustomUser.objects.get(email=self.email)
        self.assertTrue(user.check_password(self.password))

    def test_first_name_label(self):
        user = CustomUser.objects.get(id=1)
        field_label = user._meta.get_field('first_name').verbose_name
        self.assertEquals(field_label, 'first name')

    def test_last_name_label(self):
        user = CustomUser.objects.get(id=1)
        field_label = user._meta.get_field('last_name').verbose_name
        self.assertEquals(field_label, 'last name')

    def test_email_label(self):
        user = CustomUser.objects.get(id=1)
        field_label = user._meta.get_field('email').verbose_name
        self.assertEquals(field_label, 'email address')

    def test_password1_label(self):
        user = CustomUser.objects.get(id=1)
        field_label = user._meta.get_field('password').verbose_name
        self.assertEquals(field_label, 'password')

    def test_first_name_max_length(self):
        user = CustomUser.objects.get(id=1)
        max_length = user._meta.get_field('first_name').max_length
        self.assertEquals(max_length, self.first_name_max_length)

    def test_last_name_max_length(self):
        user = CustomUser.objects.get(id=1)
        max_length = user._meta.get_field('last_name').max_length
        self.assertEquals(max_length, self.last_name_max_length)

    def test_email_max_length(self):
        user = CustomUser.objects.get(id=1)
        max_length = user._meta.get_field('email').max_length
        self.assertEquals(max_length, self.email_max_length)

    def test_password_max_length(self):
        user = CustomUser.objects.get(id=1)
        max_length = user._meta.get_field('password').max_length
        self.assertEquals(max_length, self.password_max_length)

    def test_object_name_is_email(self):
        user = CustomUser.objects.get(id=1)
        expected_object_name = f'{self.email}'
        self.assertEquals(expected_object_name, str(user))

