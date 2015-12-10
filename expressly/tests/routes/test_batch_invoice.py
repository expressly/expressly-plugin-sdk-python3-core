from unittest import TestCase

from expressly import routes


class BatchInvoiceTest(TestCase):
    def setUp(self):
        self.route = routes['batch_invoice']

    def test_regex(self):
        self.assertRegex('/expressly/api/batch/invoice/', self.route.regex)
        self.assertRegex('/expressly/api/batch/invoice', self.route.regex)
        self.assertRegex('expressly/api/batch/invoice/', self.route.regex)
        self.assertRegex('expressly/api/batch/invoice', self.route.regex)

    def test_method(self):
        self.assertEqual('POST', self.route.method)

    def test_authorization(self):
        self.assertTrue(self.route.authorization)
