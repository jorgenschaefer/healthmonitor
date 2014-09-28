from features.support import HealthTestCase

# As an active user
# I want to see a table of my weight history
# In order to get an overview of my weight development.


class Test0004(HealthTestCase):
    def test_weight_history(self):
        # Given an authenticated user
        self.given_an_authenticated_user()
        # When I enter my weight
        self.open("/")
        weight_input = self.browser.find_element_by_id("weightInput")
        weight_input.send_keys("85.0")
        submit = self.browser.find_element_by_id("weightSubmit")
        submit.click()
        # Then I should see my weight in a table
        weight_table = self.browser.find_element_by_id("weightTable")
        weight = weight_table.find_element_by_css_selector(
            "tr td.weight"
        )
        self.assertEqual("85.0", weight.text)
