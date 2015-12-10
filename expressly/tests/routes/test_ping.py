from unittest import TestCase
from expressly import routes


class PingTest(TestCase):
    def setUp(self):
        self.route = routes['ping']

    def test_regex(self):
        self.assertRegex('/expressly/api/ping/', self.route.regex)
        self.assertRegex('/expressly/api/ping', self.route.regex)
        self.assertRegex('expressly/api/ping/', self.route.regex)
        self.assertRegex('expressly/api/ping', self.route.regex)

    def test_method(self):
        self.assertEqual('GET', self.route.method)

    def test_authorization(self):
        self.assertFalse(self.route.authorization)
