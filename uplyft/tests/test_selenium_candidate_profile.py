from django.urls import reverse
from django.contrib.staticfiles.testing import LiveServerTestCase
from selenium import webdriver
from uplyft.tests.resources import create_candidate_with_active_profile, test_user_data


class CandidateProfileFunctionalTests(LiveServerTestCase):
    def candidate_login(self):
        self.browser.get(
            self.live_server_url + reverse("candidate_login:candidate_login")
        )
        self.browser.find_element_by_name("username").send_keys(
            test_user_data["candidate"]["email"]
        )
        self.browser.find_element_by_name("password").send_keys(
            test_user_data["candidate"]["password"]
        )
        submit = self.browser.find_element_by_name("submit")
        submit.click()

    def go_to_candidate_profile(self):
        self.candidate_login()
        self.browser.get(self.live_server_url + "/candidate_profile/")

    def setUp(self):
        self.candidate = create_candidate_with_active_profile(
            test_user_data["candidate"]
        )
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(10)

    def tearDown(self):
        self.browser.quit()

    def test_candidate_profile_is_loaded_with_existing_active_profile_details(self):
        self.go_to_candidate_profile()
        first_name = self.browser.find_element_by_name("first_name")
        self.assertEquals(
            first_name.get_attribute("value"),
            test_user_data["candidate"]["profile"]["first_name"],
        )
        last_name = self.browser.find_element_by_name("last_name")
        self.assertEquals(
            last_name.get_attribute("value"),
            test_user_data["candidate"]["profile"]["last_name"],
        )
        address_line = self.browser.find_element_by_name("address_line")
        self.assertEquals(
            address_line.get_attribute("value"),
            test_user_data["candidate"]["profile"]["address_line"],
        )
