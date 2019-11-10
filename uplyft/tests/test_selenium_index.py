from django.urls import reverse
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver


class IndexFunctionalTests(StaticLiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(10)

    def tearDown(self):
        self.browser.quit()

    def test_GET_index_anonymous_users(self):
        self.browser.get(self.live_server_url + reverse("uplyft:index"))
        title = self.browser.find_element_by_name("title")
        welcome_message = self.browser.find_element_by_name("welcome_message")
        candidate_login_link = self.browser.find_element_by_name("candidate_login_link")
        employer_login_link = self.browser.find_element_by_name("employer_login_link")
        self.assertEquals(title.text, "UPLYFT")
        self.assertEquals(welcome_message.text, "Start a new journey!")
        self.assertEquals(candidate_login_link.text, "CANDIDATES")
        self.assertEquals(employer_login_link.text, "EMPLOYERS")

    def test_GET_index_candidate_login_link_redirects_to_candidate_login(self):
        self.browser.get(self.live_server_url + reverse("uplyft:index"))
        candidate_login_link = self.browser.find_element_by_name(
            "candidate_login_link")
        candidate_login_link.click()
        self.browser.find_element_by_name("candidate_login_form")

    def test_GET_index_employer_login_link_redirects_to_employer_login(self):
        self.browser.get(self.live_server_url + reverse("uplyft:index"))
        employer_login_link = self.browser.find_element_by_name(
            "employer_login_link")
        employer_login_link.click()
        self.browser.find_element_by_name("employer_login_form")