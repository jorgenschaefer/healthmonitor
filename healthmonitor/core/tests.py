from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

from healthmonitor.core import support


class TestLoginView(support.ViewTestCase):
    def test_should_display_login_form(self):
        with self.assertTemplateUsed('core/login.html'):
            self.client.get(reverse('login'))

    def test_should_log_in(self):
        User.objects.create_user(
            username="testuser",
            email="testuser@localhost.tld",
            password="12345"
        )

        response = self.client.post(reverse('login') +
                                    "?next=" +
                                    reverse('home'),
                                    {'username': "testuser",
                                     'password': "12345"})

        self.assertRedirects(response, reverse('home'))

    def test_should_show_errors_on_false_login(self):
        with self.assertTemplateUsed('core/login.html'):
            response = self.client.post(reverse('login') +
                                        "?next=" +
                                        reverse('home'),
                                        {'username': "testuser",
                                         'password': "wrong"},
                                        follow=True)

        self.assertContains(response,
                            "Your username and password didn")
