from unittest import TestCase
from expressly import routes


class UserTest(TestCase):
    def setUp(self):
        self.route = routes['user']

    def test_regex(self):
        self.assertRegex('/expressly/api/user/test@test.com/', self.route.regex)
        self.assertRegex('/expressly/api/user/test@test.com', self.route.regex)
        self.assertRegex('expressly/api/user/test@test.com/', self.route.regex)
        self.assertRegex('expressly/api/user/test@test.com', self.route.regex)

    def test_method(self):
        self.assertEqual('GET', self.route.method)

    def test_authorization(self):
        self.assertTrue(self.route.authorization)
