from django.urls import reverse
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from uplyft.tests.resources import create_department, create_employer, test_user_data


class EmployerLoginFunctionalTests(StaticLiveServerTestCase):
    def setUp(self):
        self.department = create_department(test_user_data["department"])
        self.employer = create_employer(self.department, test_user_data["employer"])
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(10)

    def tearDown(self):
        self.browser.quit()

    def test_employer_login_and_redirect_to_dashboard(self):
        self.browser.get(self.live_server_url + reverse("uplyft:index"))
        employer_login_link = self.browser.find_element_by_name("employer_login_link")
        employer_login_link.click()
        email_input = self.browser.find_element_by_name("username")
        email_input.send_keys(test_user_data["employer"]["email"])
        password_input = self.browser.find_element_by_name("password")
        password_input.send_keys(test_user_data["employer"]["password"])
        submit = self.browser.find_element_by_name("submit")
        submit.click()
        dashboard_headline = self.browser.find_element_by_tag_name("h1").text
        expected_headline = (
                "Welcome back, " + test_user_data["employer"]["first_name"] + "."
        )
        self.assertEqual(dashboard_headline, expected_headline)
