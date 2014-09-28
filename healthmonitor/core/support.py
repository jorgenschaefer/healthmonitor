from django.conf import settings
from django.utils import dateformat
from django.test import TestCase, Client
from django.contrib.auth.models import User


class ViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def create_user(self):
        return User.objects.create_user(
            username="testuser",
            email="testuser@localhost.tld",
            password="12345"
        )

    def login(self):
        self.user = self.create_user()
        self.client.login(username='testuser', password='12345')


def formatted_date(date):
    """Return the default formatted version of date."""
    df = dateformat.DateFormat(date)
    return df.format(settings.DATE_FORMAT)
