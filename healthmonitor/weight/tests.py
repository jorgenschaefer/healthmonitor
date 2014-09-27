from django.contrib.auth.models import User
from django.core.urlresolvers import resolve, reverse
from django.test import TestCase, Client

from . import views


class ViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()


class TestHomeView(ViewTestCase):
    def test_should_be_at_root(self):
        actual = resolve('/')

        self.assertEqual(views.home, actual.func)

    def test_should_redirect_anonymous_users_to_login_page(self):
        response = self.client.get(reverse('home'))

        self.assertRedirects(
            response,
            reverse('login') + "?next=" + reverse('home')
        )

    def test_should_not_redirect_authenticated_users(self):
        User.objects.create_user(
            username="testuser",
            email="testuser@localhost.tld",
            password="12345"
        )
        self.client.login(username='testuser', password='12345')

        with self.assertTemplateUsed('weight/home.html'):
            self.client.get(reverse('home'))
