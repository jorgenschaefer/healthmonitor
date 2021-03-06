from django.utils import timezone

from features.support import HealthTestCase
from healthmonitor.weight.models import Weight

# As an authenticated user
# I want to enter my current weight
# In order to easily update my weight history


class Test0002(HealthTestCase):
    def test_weight_form(self):
        # Given an authenticated user
        self.given_an_authenticated_user()
        # When I go to the main page
        self.open("/")
        # Then I should be able to enter my current weight
        weight_input = self.browser.find_element_by_id("weightInput")
        weight_input.send_keys("85.0")
        submit = self.browser.find_element_by_id("weightSubmit")
        submit.click()
        # And I should find the weight in the database
        weight = Weight.objects.get()
        self.assertEqual(timezone.now().date(), weight.date)
        self.assertAlmostEqual(85.0, weight.weight)

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
