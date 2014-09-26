from features.support import SeleniumTestCase


class Test0001(SeleniumTestCase):
    def test_foo(self):
        self.open("/")

        self.assertEqual("Welcome to Django", self.browser.title)
