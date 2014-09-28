from django.core.urlresolvers import resolve, reverse

from . import views, models
from healthmonitor.core import support


class TestHomeView(support.ViewTestCase):
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
        self.login()
        with self.assertTemplateUsed('weight/home.html'):
            self.client.get(reverse('home'))

    def test_should_have_weight_form(self):
        self.login()
        response = self.client.get(reverse('home'))
        self.assertContains(response, "weightInput")
        self.assertContains(response, "weightSubmit")

    def test_should_store_weight(self):
        self.login()
        self.client.post(
            reverse('home'),
            {'weight': 85.0}
        )
        weight = models.Weight.objects.get()
        self.assertEqual(weight.user, self.user)
        self.assertEqual(weight.weight, 85.0)
