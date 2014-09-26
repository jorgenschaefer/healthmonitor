import os

from django import test
from selenium import webdriver


PHANTOMJS_BIN = os.path.join(
    os.path.dirname(__file__),
    "..",
    "node_modules/phantomjs/lib/phantom/bin/phantomjs"
)


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
            self.browser = webdriver.PhantomJS(PHANTOMJS_BIN)
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def open(self, url):
        self.browser.get("{}{}".format(self.live_server_url, url))
