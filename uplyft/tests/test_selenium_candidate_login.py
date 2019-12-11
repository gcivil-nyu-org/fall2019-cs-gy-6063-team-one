from django.urls import reverse
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from uplyft.tests.resources import create_candidate_with_active_profile, test_user_data
from uplyft.tests.decorators import setUpMockedS3Selenium

setUpMockedS3Selenium()


class CandidateLoginFunctionalTests(StaticLiveServerTestCase):
    def setUp(self):
        self.candidate = create_candidate_with_active_profile(
            test_user_data["candidate"]
        )
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(10)

    def tearDown(self):
        self.browser.quit()

    def test_candidate_login_redirect_to_dashboard(self):
        self.browser.get(self.live_server_url + reverse("candidate_login:candidate_login"))
        self.browser.find_element_by_name("username").send_keys(
            test_user_data["candidate"]["email"]
        )
        self.browser.find_element_by_name("password").send_keys(
            test_user_data["candidate"]["password"]
        )
        submit = self.browser.find_element_by_name("submit")
        submit.click()
        dashboard_headline = self.browser.find_element_by_tag_name("h1").text
        expected_headline = (
            "Welcome back, " + test_user_data["candidate"]["first_name"] + "."
        )
        self.assertEqual(dashboard_headline, expected_headline)
