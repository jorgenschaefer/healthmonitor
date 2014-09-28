import os

from django import test
from django.contrib.auth.models import User
from selenium import webdriver


class SeleniumTestCase(test.LiveServerTestCase):
    def setUp(self):
        if os.environ.get('WEBDRIVER') == "firefox":
            # When running ff, we do this usually via sshfs, which
            # breaks the webdriver.
            try:
                olddir = os.getcwd()
                os.chdir("/")
                self.browser = webdriver.Firefox()
            finally:
                os.chdir(olddir)
        else:
            # Can't chdir for phantomjs, that breaks ghostdriver.log
            # creation
            self.browser = webdriver.PhantomJS()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def open(self, url):
        self.browser.get("{}{}".format(self.live_server_url, url))


class HealthTestCase(SeleniumTestCase):
    def given_an_authenticated_user(self):
        User.objects.create_user(
            username="testuser",
            email="testuser@localhost.tld",
            password="12345"
        )
        self.open("/")
        username = self.browser.find_element_by_name("username")
        password = self.browser.find_element_by_name("password")
        submit = self.browser.find_element_by_id("loginSubmit")
        username.send_keys("testuser")
        password.send_keys("12345")
        submit.click()
