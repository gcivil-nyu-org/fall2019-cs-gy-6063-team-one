from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver


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
        self.browser.get("http://localhost:8001/jobs")
        assert "Uplyft" in self.browser.title, "Browser title was " + self.browser.title

    # This section will be reactivated when login for testing is finished
    # def test_input_search(self):
    #     self.browser.get("http://localhost:8001/jobs")
    #     input_search_terms = self.browser.grabElement("q")
    #     input_search_terms.send_keys(self.q)
    #     input_search_terms.send_keys(Keys.RETURN)
    #     job_cards = self.browser.find_elements_by_class_name("card")
    #     print(len(job_cards))
    #     for card in job_cards:
    #         print(card)
