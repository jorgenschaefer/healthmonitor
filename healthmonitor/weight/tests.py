from django.core.urlresolvers import resolve, reverse
from django.utils import timezone

from . import views, models
from healthmonitor.core import support


class TestWeightModel(support.ViewTestCase):
    def test_string_version(self):
        date = timezone.now().date()
        user = self.create_user()
        weight = models.Weight.objects.create(
            user=user,
            date=date,
            weight=85.0
        )
        self.assertEqual("testuser at 85.0 kg on {}"
                         .format(weight.date),
                         str(weight))


class TestHomeView(support.ViewTestCase):
    def create_weight(self, weight):
        user = self.user
        date = timezone.now().date()
        return models.Weight.objects.create(
            user=user,
            date=date,
            weight=weight
        )

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

    def test_should_show_weight_history(self):
        self.login()
        weight = self.create_weight(weight=85.0)

        response = self.client.get(reverse('home'))

        self.assertContains(response, support.formatted_date(weight.date))
        self.assertContains(response, "85.0")

    def test_should_overwrite_old_entries_for_the_same_date(self):
        self.login()
        self.create_weight(weight=85.0)

        self.client.post(
            reverse('home'),
            {'weight': 82.0}
        )

        weight = models.Weight.objects.get()
        self.assertAlmostEqual(82.0, weight.weight)
