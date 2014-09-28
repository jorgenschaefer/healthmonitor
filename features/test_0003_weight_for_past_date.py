from features.support import HealthTestCase

from healthmonitor.weight.models import Weight

# As an authenticated user
# I want to enter my weight for a past date
# In order to complete my weight history in case I forgot an entry.


class Test0003(HealthTestCase):
    def test_weight_form(self):
        # Given an authenticated user
        self.given_an_authenticated_user()
        # When I go to the main page
        self.open("/")
        # Then I should be able to enter my current weight
        weight_input = self.browser.find_element_by_id("weightInput")
        weight_input.send_keys("85.0")
        # And the current date
        date_input = self.browser.find_element_by_id("dateInput")
        date_input.clear()
        date_input.send_keys("2000-09-01")
        submit = self.browser.find_element_by_id("weightSubmit")
        submit.click()
        # And I should find the new weight in the database
        weight = Weight.objects.get()
        self.assertEqual("2000-09-01", weight.date.strftime("%Y-%m-%d"))

    def test_should_not_duplicate_weights(self):
        # Given an authenticated user
        self.given_an_authenticated_user()
        # When I go to the main page
        self.open("/")
        # And I enter my current weight
        weight_input = self.browser.find_element_by_id("weightInput")
        weight_input.send_keys("85.0")
        submit = self.browser.find_element_by_id("weightSubmit")
        submit.click()
        # And I enter my current weight again
        weight_input = self.browser.find_element_by_id("weightInput")
        weight_input.send_keys("85.0")
        submit = self.browser.find_element_by_id("weightSubmit")
        submit.click()
        # Then there should still be only one weight value
        Weight.objects.get()
