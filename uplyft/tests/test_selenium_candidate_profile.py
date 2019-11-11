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
        self.browser.get(self.live_server_url + reverse("dashboard:dashboard"))
        profile_link = self.browser.find_element_by_name("candidate_profile_link")
        profile_link.click()

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

    def test_candidate_profile_update_first_name(self):
        self.go_to_candidate_profile()
        first_name_before = self.browser.find_element_by_name("first_name")
        self.assertEquals(
            first_name_before.get_attribute("value"),
            test_user_data["candidate"]["profile"]["first_name"],
        )
        first_name_before.clear()
        first_name_before.send_keys(
            test_user_data["candidate"]["new_profile"]["first_name"]
        )
        submit_button = self.browser.find_element_by_name("submit")
        submit_button.click()
        first_name_after = self.browser.find_element_by_name("first_name")
        self.assertEquals(
            first_name_after.get_attribute("value"),
            test_user_data["candidate"]["new_profile"]["first_name"],
        )

    def test_candidate_profile_update_last_name(self):
        self.go_to_candidate_profile()
        last_name_before = self.browser.find_element_by_name("last_name")
        self.assertEquals(
            last_name_before.get_attribute("value"),
            test_user_data["candidate"]["profile"]["last_name"],
        )
        last_name_before.clear()
        last_name_before.send_keys(
            test_user_data["candidate"]["new_profile"]["last_name"]
        )
        submit_button = self.browser.find_element_by_name("submit")
        submit_button.click()
        last_name_after = self.browser.find_element_by_name("last_name")
        self.assertEquals(
            last_name_after.get_attribute("value"),
            test_user_data["candidate"]["new_profile"]["last_name"],
        )

    def test_candidate_profile_update_email(self):
        self.go_to_candidate_profile()
        email_before = self.browser.find_element_by_name("email")
        self.assertEquals(
            email_before.get_attribute("value"),
            test_user_data["candidate"]["profile"]["email"],
        )
        email_before.clear()
        email_before.send_keys(test_user_data["candidate"]["new_profile"]["email"])
        submit_button = self.browser.find_element_by_name("submit")
        submit_button.click()
        email_after = self.browser.find_element_by_name("email")
        self.assertEquals(
            email_after.get_attribute("value"),
            test_user_data["candidate"]["new_profile"]["email"],
        )

    def test_candidate_profile_update_address(self):
        self.go_to_candidate_profile()
        address_before = self.browser.find_element_by_name("address_line")
        self.assertEquals(
            address_before.get_attribute("value"),
            test_user_data["candidate"]["profile"]["address_line"],
        )
        address_before.clear()
        address_before.send_keys(
            test_user_data["candidate"]["new_profile"]["address_line"]
        )
        submit_button = self.browser.find_element_by_name("submit")
        submit_button.click()
        address_after = self.browser.find_element_by_name("address_line")
        self.assertEquals(
            address_after.get_attribute("value"),
            test_user_data["candidate"]["new_profile"]["address_line"],
        )

    def test_candidate_profile_update_zip_code(self):
        self.go_to_candidate_profile()
        zip_code_before = self.browser.find_element_by_name("zip_code")
        self.assertEquals(
            zip_code_before.get_attribute("value"),
            test_user_data["candidate"]["profile"]["zip_code"],
        )
        zip_code_before.clear()
        zip_code_before.send_keys(
            test_user_data["candidate"]["new_profile"]["zip_code"]
        )
        submit_button = self.browser.find_element_by_name("submit")
        submit_button.click()
        zip_code_after = self.browser.find_element_by_name("zip_code")
        self.assertEquals(
            zip_code_after.get_attribute("value"),
            test_user_data["candidate"]["new_profile"]["zip_code"],
        )

    def test_candidate_profile_update_state(self):
        self.go_to_candidate_profile()
        state_before = self.browser.find_element_by_name("state")
        self.assertEquals(
            state_before.get_attribute("value"),
            test_user_data["candidate"]["profile"]["state"],
        )
        for option in state_before.find_elements_by_tag_name("option"):
            if (
                option.text
                == test_user_data["candidate"]["new_profile"]["state_display"]
            ):
                option.click()
                break
        submit_button = self.browser.find_element_by_name("submit")
        submit_button.click()
        state_after = self.browser.find_element_by_name("state")
        self.assertEquals(
            state_after.get_attribute("value"),
            test_user_data["candidate"]["new_profile"]["state"],
        )

    def test_candidate_profile_update_gender(self):
        self.go_to_candidate_profile()
        gender_before = self.browser.find_element_by_name("gender")
        self.assertEquals(
            gender_before.get_attribute("value"),
            test_user_data["candidate"]["profile"]["gender"],
        )
        for option in gender_before.find_elements_by_tag_name("option"):
            if (
                option.text
                == test_user_data["candidate"]["new_profile"]["gender_display"]
            ):
                option.click()
                break
        submit_button = self.browser.find_element_by_name("submit")
        submit_button.click()
        gender_after = self.browser.find_element_by_name("gender")
        self.assertEquals(
            gender_after.get_attribute("value"),
            test_user_data["candidate"]["new_profile"]["gender"],
        )

    def test_candidate_profile_update_health_conditions(self):
        self.go_to_candidate_profile()
        health_conditions_before = self.browser.find_element_by_name(
            "health_conditions"
        )
        self.assertEquals(
            health_conditions_before.get_attribute("value"),
            test_user_data["candidate"]["profile"]["health_conditions"],
        )
        for option in health_conditions_before.find_elements_by_tag_name("option"):
            if (
                option.text
                == test_user_data["candidate"]["new_profile"][
                    "health_conditions_display"
                ]
            ):
                option.click()
                break
        submit_button = self.browser.find_element_by_name("submit")
        submit_button.click()
        health_conditions_after = self.browser.find_element_by_name("health_conditions")
        self.assertEquals(
            health_conditions_after.get_attribute("value"),
            test_user_data["candidate"]["new_profile"]["health_conditions"],
        )

    def test_candidate_profile_update_veteran_status(self):
        self.go_to_candidate_profile()
        veteran_status_before = self.browser.find_element_by_name("veteran")
        self.assertEquals(
            veteran_status_before.get_attribute("value"),
            test_user_data["candidate"]["profile"]["veteran"],
        )
        for option in veteran_status_before.find_elements_by_tag_name("option"):
            if (
                option.text
                == test_user_data["candidate"]["new_profile"]["veteran_display"]
            ):
                option.click()
                break
        submit_button = self.browser.find_element_by_name("submit")
        submit_button.click()
        veteran_status_after = self.browser.find_element_by_name("veteran")
        self.assertEquals(
            veteran_status_after.get_attribute("value"),
            test_user_data["candidate"]["new_profile"]["veteran"],
        )

    def test_candidate_profile_update_race(self):
        self.go_to_candidate_profile()
        race_before = self.browser.find_element_by_name("race")
        self.assertEquals(
            race_before.get_attribute("value"),
            test_user_data["candidate"]["profile"]["race"],
        )
        for option in race_before.find_elements_by_tag_name("option"):
            if (
                option.text
                == test_user_data["candidate"]["new_profile"]["race_display"]
            ):
                option.click()
                break
        submit_button = self.browser.find_element_by_name("submit")
        submit_button.click()
        race_after = self.browser.find_element_by_name("race")
        self.assertEquals(
            race_after.get_attribute("value"),
            test_user_data["candidate"]["new_profile"]["race"],
        )

    def test_candidate_profile_update_ethnicity(self):
        self.go_to_candidate_profile()
        ethnicity_before = self.browser.find_element_by_name("ethnicity")
        self.assertEquals(
            ethnicity_before.get_attribute("value"),
            test_user_data["candidate"]["profile"]["ethnicity"],
        )
        for option in ethnicity_before.find_elements_by_tag_name("option"):
            if (
                option.text
                == test_user_data["candidate"]["new_profile"]["ethnicity_display"]
            ):
                option.click()
                break
        submit_button = self.browser.find_element_by_name("submit")
        submit_button.click()
        ethnicity_after = self.browser.find_element_by_name("ethnicity")
        self.assertEquals(
            ethnicity_after.get_attribute("value"),
            test_user_data["candidate"]["new_profile"]["ethnicity"],
        )

    def test_candidate_navigate_to_profile(self):
        self.candidate_login()
        self.browser.get(self.live_server_url + reverse("dashboard:dashboard"))
        profile_link = self.browser.find_element_by_name("candidate_profile_link")
        profile_link.click()
        self.browser.find_element_by_name("address_line").send_keys(
            test_user_data["candidate"]["profile"]["address_line"]
        )
        submit_button = self.browser.find_element_by_name("submit")
        submit_button.click()
        self.browser.get(self.live_server_url + reverse("dashboard:dashboard"))
        profile_link = self.browser.find_element_by_name("candidate_profile_link")
        profile_link.click()
        profile_title = self.browser.find_element_by_tag_name("h1")
        self.assertEquals(profile_title.text, "Your Profile")
