from django.test import TestCase

from uplyft.tests.resources import test_user_data
from uplyft.models import CustomUser


class GeneralTests(TestCase):
    def test_create_superuser(self):
        superuser = CustomUser.objects.create_user(
            email=test_user_data["candidate"]["email"],
            password=test_user_data["candidate"]["password"],
            first_name=test_user_data["candidate"]["first_name"],
            last_name=test_user_data["candidate"]["last_name"],
            is_candidate=False,
            is_superuser=True,
            is_active=True,
        )
        self.assertIsNotNone(superuser)
        self.assertEquals(CustomUser.objects.all().count(), 1)
