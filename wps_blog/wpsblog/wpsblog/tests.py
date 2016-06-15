from django.test import TestCase
from django.core.urlresolvers import reverse

class HomeViewTestCase(TestCase):

    def setUp(self):
        self.response = self.client.get(reverse("pricing"))

    def test_homeview_should_return_200(self):
        self.assertEqual(
                self.response.status_code,
                200,
         )

