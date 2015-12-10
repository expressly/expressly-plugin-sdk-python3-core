from unittest import TestCase

from expressly import routes


class BatchCustomerTest(TestCase):
    def setUp(self):
        self.route = routes['batch_customer']

    def test_regex(self):
        self.assertRegex('/expressly/api/batch/customer/', self.route.regex)
        self.assertRegex('/expressly/api/batch/customer', self.route.regex)
        self.assertRegex('expressly/api/batch/customer/', self.route.regex)
        self.assertRegex('expressly/api/batch/customer', self.route.regex)

    def test_method(self):
        self.assertEqual('POST', self.route.method)

    def test_authorization(self):
        self.assertTrue(self.route.authorization)
