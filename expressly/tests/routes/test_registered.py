from unittest import TestCase
from expressly import routes


class RegisteredTest(TestCase):
    def setUp(self):
        self.route = routes['registered']

    def test_route(self):
        self.assertRegex('/expressly/api/registered/', self.route.regex)
        self.assertRegex('/expressly/api/registered', self.route.regex)
        self.assertRegex('expressly/api/registered/', self.route.regex)
        self.assertRegex('expressly/api/registered', self.route.regex)

    def test_method(self):
        self.assertEqual('GET', self.route.method)

    def test_authorization(self):
        self.assertTrue(self.route.authorization)
