from features.support import SeleniumTestCase

from django.contrib.auth.models import User

# As an unauthenticated user
# I want to be able to log in
# In order to use the features of the site


class Test0001(SeleniumTestCase):
    def test_login_prompt(self):
        # Given an unauthenticated user
        # When I open the main page
        self.open("/")
        # Then I should see a login prompt
        self.browser.find_element_by_name("username")
        self.browser.find_element_by_name("password")

    def test_login_success(self):
        # Given an unauthenticated user
        User.objects.create_user(
            username="testuser",
            email="testuser@localhost.tld",
            password="12345"
        )
        # When I open the main page
        self.open("/")
        # And fill in my login details
        username = self.browser.find_element_by_name("username")
        password = self.browser.find_element_by_name("password")
        submit = self.browser.find_element_by_id("loginSubmit")
        username.send_keys("testuser")
        password.send_keys("12345")
        submit.click()
        # Then I should see a welcome screen
        text_field = self.browser.find_element_by_css_selector(
            'div.navbar p.navbar-text'
        )
        self.assertIn("Logged in as testuser", text_field.text)

    def test_login_error(self):
        # Given an unauthenticated user
        # When I open the main page
        self.open("/")
        # And fill in wrong login details
        username = self.browser.find_element_by_name("username")
        password = self.browser.find_element_by_name("password")
        submit = self.browser.find_element_by_id("loginSubmit")
        username.send_keys("bla bla")
        password.send_keys("wrong")
        submit.click()
        # Then I should see a login prompt
        self.browser.find_element_by_name("username")
        self.browser.find_element_by_name("password")
        # And I should see "Your username and password didn't match"
        form_error = self.browser.find_element_by_css_selector(
            "#formErrors p"
        )
        self.assertIn("Your username and password didn", form_error.text)
