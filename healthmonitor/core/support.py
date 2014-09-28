from django.test import TestCase, Client
from django.contrib.auth.models import User


class ViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def login(self):
        self.user = User.objects.create_user(
            username="testuser",
            email="testuser@localhost.tld",
            password="12345"
        )
        self.client.login(username='testuser', password='12345')
