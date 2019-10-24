from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from tests.tests import valid_data

from django.contrib.auth import get_user_model
from django.test import TestCase

from jobs.models import Job


class JobsSearchFormTest(StaticLiveServerTestCase):
    q = ""
    port = 8001

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def grabElement(self, name):
        return self.browser.find_element_by_name(name)

    def test_jobs_title(self):
        self.browser.get('http://localhost:8001/jobs')
        assert 'Uplyft' in self.browser.title, "Browser title was " + self.browser.title

    def test_input_search(self):
        self.browser.get('http://localhost:8001/jobs')
        input_search_terms = self.grabElement("q")
        input_search_terms.send_keys(self.q)
        input_search_terms.send_keys(Keys.RETURN)
        job_cards = self.browser.find_elements_by_class_name("card")
        print(len(job_cards))
        for card in job_cards:
            print(card)

