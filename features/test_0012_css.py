from features.support import SeleniumTestCase

# Include CSS


class Test0012(SeleniumTestCase):
    def test_should_include_css(self):
        # Given an unauthenticated user
        # When I open the main page
        self.open("/")
        # Then I should see a CSS tag
        link = self.browser.find_element_by_tag_name("link")
        self.assertIn('static/CACHE/css', link.get_attribute("href"))
