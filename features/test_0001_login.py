from features.support import SeleniumTestCase

# As an unauthenticated user
# I want to be able to log in
# In order to use the features of the site


class Test0001(SeleniumTestCase):
    def runTest(self):
        # Given an unauthenticated user
        # When open the main page
        self.open("/")
        # I should see a login prompt
        self.browser.find_element_by_name("username")
        self.browser.find_element_by_name("password")
