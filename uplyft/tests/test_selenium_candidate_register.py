from django.urls import reverse
from django.contrib.staticfiles.testing import LiveServerTestCase
from selenium import webdriver
from uplyft.tests.resources import test_user_data


class CandidateRegisterFunctionalTests(LiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(10)

    def tearDown(self):
        self.browser.quit()

    def test_candidate_registration(self):
        self.browser.get(self.live_server_url + reverse("uplyft:index"))
        candidate_login_link = self.browser.find_element_by_name("candidate_login_link")
        candidate_login_link.click()
        registration_link = self.browser.find_element_by_name("candidate_register_link")
        registration_link.click()
        self.browser.find_element_by_name("first_name").send_keys(
            test_user_data["candidate"]["first_name"]
        )
        self.browser.find_element_by_name("last_name").send_keys(
            test_user_data["candidate"]["last_name"]
        )
        self.browser.find_element_by_name("email").send_keys(
            test_user_data["candidate"]["email"]
        )
        self.browser.find_element_by_name("password1").send_keys(
            test_user_data["candidate"]["password"]
        )
        self.browser.find_element_by_name("password2").send_keys(
            test_user_data["candidate"]["password"]
        )
        submit_button = self.browser.find_element_by_name("submit")
        submit_button.click()
        dashboard_title = self.browser.find_element_by_tag_name("h1")
        self.assertEquals(dashboard_title.text, "Dashboard")
